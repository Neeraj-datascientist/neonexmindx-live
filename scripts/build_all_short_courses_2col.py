import docx
import re
import os
import shutil

def parse_docx_modules(file_path):
    doc = docx.Document(file_path)
    modules = []
    cur_mod = None
    
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t: continue
        
        # Check if heading starts a new module
        is_mod_header = False
        if t.startswith(('MODULE ', 'Module ')) or (t[0].isdigit() and ('.' in t[:4]) and (' ' in t[:6]) and len(t) < 70 and not any(t.startswith(f"{x}.") for x in [f"{i}.{j}" for i in range(1,30) for j in range(1,30)])):
            is_mod_header = True
            
        # Match "1. Title", "2. Title", etc. (excluding 1.1, 1.2)
        match_num = re.match(r'^(\d+)\.\s+([^\d].*)$', t)
        match_mod = re.match(r'^MODULE\s+(\d+)[\s:—-]+(.*)$', t, re.I)
        
        if match_mod:
            if cur_mod: modules.append(cur_mod)
            num = f"{int(match_mod.group(1)):02d}"
            title = match_mod.group(2).strip()
            cur_mod = {'num': num, 'title': title, 'topics': []}
        elif match_num and len(t) < 70 and not t.lower().startswith(('note', 'assignment')):
            if cur_mod: modules.append(cur_mod)
            num = f"{int(match_num.group(1)):02d}"
            title = match_num.group(2).strip()
            cur_mod = {'num': num, 'title': title, 'topics': []}
        elif cur_mod:
            # Topic bullet
            if t.startswith(('•', '-', '*')):
                clean = t.lstrip('•-* ').strip()
                if clean: cur_mod['topics'].append(clean)
            elif re.match(r'^\d+\.\d+\s+', t):
                clean = re.sub(r'^\d+\.\d+\s*', '', t).strip()
                if clean: cur_mod['topics'].append(clean)
            elif len(t) < 90 and not t.lower().startswith(('objective', 'stage', 'p.')):
                cur_mod['topics'].append(t)
                
    if cur_mod: modules.append(cur_mod)
    return modules

# Parse Python
py_mods = parse_docx_modules(r'deployment_NeoNex\syllabus\individual modules\Python (4).docx')
print(f"Parsed {len(py_mods)} Python modules.")

# Parse SQL
sql_mods = parse_docx_modules(r'deployment_NeoNex\syllabus\individual modules\SQL  (3).docx')
print(f"Parsed {len(sql_mods)} SQL modules.")

# Parse ML
ml_mods = parse_docx_modules(r'deployment_NeoNex\syllabus\individual modules\MACHINE LEARNING — COMPLETE ROADMAP (2).docx')
print(f"Parsed {len(ml_mods)} ML modules.")

def build_2col_grid_html(modules, course_name):
    cards_html = []
    for i, m in enumerate(modules):
        n = m['num']
        title = m['title']
        topics = m.get('topics', [])
        # Take top 6-8 topics so cards are clean and proportional
        display_topics = topics[:8] if len(topics) > 8 else topics
        
        topics_list = "".join([f'''<li style="display:flex;align-items:flex-start;gap:10px;margin-bottom:9px;font-size:13.5px;color:#334155;line-height:1.45;">
      <svg style="width:16px;height:16px;min-width:16px;color:#16a34a;margin-top:2px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      <span>{t}</span>
    </li>''' for t in display_topics])

        open_attr = " open" if i in [0, 2] else ""
        
        card = f'''<details class="module-card"{open_attr} style="border:1px solid #e2e8f0;border-radius:14px;background:#ffffff;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,0.02);overflow:hidden;transition:all .2s ease;">
  <summary class="module-toggle" style="list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;padding:16px 20px;gap:16px;background:#ffffff;">
    <div style="display:flex;align-items:center;gap:14px;">
      <span class="module-num" style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:36px;border-radius:8px;background:#eff6ff;color:#1d4ed8;font-weight:700;font-size:14px;">{n}</span>
      <strong style="font-size:15px;color:#0f172a;font-weight:700;line-height:1.35;">{title}</strong>
    </div>
    <span class="plus" aria-hidden="true" style="font-size:20px;color:#2563eb;font-weight:600;min-width:20px;text-align:right;">+</span>
  </summary>
  <div class="module-panel" style="padding:16px 20px 18px;border-top:1px solid #f1f5f9;background:#ffffff;">
    <ul style="list-style:none;padding:0;margin:0;">
      {topics_list}
    </ul>
  </div>
</details>'''
        cards_html.append(card)

    col1_cards = "\n".join(cards_html[0::2])
    col2_cards = "\n".join(cards_html[1::2])

    return f'''
<div class="course-modules-toolbar" style="display:flex;justify-content:space-between;align-items:center;background:#f8fafc;border:1px solid #e2e8f0;padding:12px 18px;border-radius:12px;margin:20px 0 20px;flex-wrap:wrap;gap:10px;">
  <span style="font-size:13.5px;color:#334155;font-weight:600;">Course Modules &amp; Topics: <strong style="color:#0f172a;">Complete {len(modules)}-Module Curriculum</strong></span>
  <div style="display:flex;gap:8px;">
    <button type="button" class="btn-toggle-course-modules" id="btn-course-expand-all" style="background:#ffffff;border:1px solid #cbd5e1;padding:6px 14px;border-radius:8px;font-size:12.5px;font-weight:600;color:#1e293b;cursor:pointer;transition:all .15s ease;">Expand All Topics</button>
    <button type="button" class="btn-toggle-course-modules" id="btn-course-collapse-all" style="background:#ffffff;border:1px solid #cbd5e1;padding:6px 14px;border-radius:8px;font-size:12.5px;font-weight:600;color:#1e293b;cursor:pointer;transition:all .15s ease;">Collapse All</button>
  </div>
</div>

<div class="curriculum-grid-2col" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 520px), 1fr));gap:16px;align-items:start;">
  <div class="curriculum-col-left">
    {col1_cards}
  </div>
  <div class="curriculum-col-right">
    {col2_cards}
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {{
  var cards = document.querySelectorAll('.curriculum-grid-2col details.module-card');
  var expBtn = document.getElementById('btn-course-expand-all');
  var colBtn = document.getElementById('btn-course-collapse-all');
  if (expBtn) {{
    expBtn.addEventListener('click', function() {{
      cards.forEach(function(c) {{ c.open = true; }});
    }});
  }}
  if (colBtn) {{
    colBtn.addEventListener('click', function() {{
      cards.forEach(function(c) {{ c.open = false; }});
    }});
  }}
}});
</script>
'''

# Function to inject into page
def inject_curriculum(file_path, new_html):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    start_pos = html.find('<div class="curriculum">')
    if start_pos == -1: start_pos = html.find('<div class="curriculum-wrapper">')
    if start_pos == -1: start_pos = html.find('<div class="curriculum-grid-2col">')
    if start_pos == -1:
        start_pos = html.find('id="curriculum"')
        phase_end = html.find('</div></div>', start_pos)
        start_pos = phase_end + 12
        
    end_pos = html.find('</div>\n</div>\n</section>', start_pos)
    if end_pos == -1: end_pos = html.find('</div></div></section>', start_pos)
    if end_pos == -1:
        end_pos = html.find('</section>', start_pos)
        sub = html[start_pos:end_pos]
        last_div = sub.rfind('</div>')
        end_pos = start_pos + last_div
        
    html = html[:start_pos] + '\n<div class="curriculum-wrapper">\n' + new_html + '\n</div>\n' + html[end_pos:]
    
    if '.curriculum-grid-2col details[open] .plus' not in html:
        style_inject = '''<style>
.curriculum-grid-2col details[open] .plus { transform: rotate(45deg); display: inline-block; color: #dc2626 !important; }
.curriculum-grid-2col details summary::-webkit-details-marker { display:none; }
.curriculum-grid-2col details summary::marker { display:none; }
.curriculum-grid-2col details[open] { border-color: #bfdbfe !important; box-shadow: 0 4px 14px rgba(37,99,235,0.06) !important; }
</style>'''
        html = html.replace('</head>', style_inject + '\n</head>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Successfully updated {file_path}")

# Update Python
py_html = build_2col_grid_html(py_mods, "Python")
inject_curriculum(r'deployment_NeoNex\courses\python-programming-course\index.html', py_html)

# Update SQL
sql_html = build_2col_grid_html(sql_mods, "SQL")
inject_curriculum(r'deployment_NeoNex\courses\sql-course\index.html', sql_html)

# Update Machine Learning
ml_html = build_2col_grid_html(ml_mods, "Machine Learning")
inject_curriculum(r'deployment_NeoNex\courses\machine-learning-course\index.html', ml_html)
