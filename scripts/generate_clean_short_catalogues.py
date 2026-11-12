import docx
import re
import os

def clean_text(s):
    return s.strip()

# ==========================================
# 1. PARSE SQL DOCX
# ==========================================
def parse_sql_docx(docx_path):
    doc = docx.Document(docx_path)
    raw_paras = [clean_text(p.text) for p in doc.paragraphs if clean_text(p.text)]
    
    modules = []
    current_module = None
    
    # We want modules to be:
    # 1. Introduction to SQL & RDBMS
    # 2. SQL Classification
    # 3. Creating & Managing Databases
    # ... up to 23. Triggers
    
    mod_pattern = re.compile(r'^(\d+)\.\s+(.*)')
    
    for p in raw_paras:
        # Check if start is like "SQL \n 1. Introduction to SQL & RDBMS"
        p_lines = [l.strip() for l in p.split('\n') if l.strip()]
        for line in p_lines:
            if line.upper() == 'SQL':
                continue
            
            # Check for module header: "1. Introduction to SQL & RDBMS", etc.
            # But avoid subtopics like "1.1 What is SQL?" or "13.1 UNION"
            m = mod_pattern.match(line)
            is_main_mod = False
            if m:
                num = int(m.group(1))
                rest = m.group(2)
                # It is a main module if it doesn't have a dot right after the number, e.g. not "1.1"
                if not line.startswith(f"{num}."):
                    is_main_mod = False
                elif not re.match(r'^\d+\.\d+', line):
                    is_main_mod = True
                    
            if is_main_mod:
                if current_module:
                    modules.append(current_module)
                current_module = {
                    'num': m.group(1),
                    'title': line,
                    'topics': []
                }
            else:
                if current_module is None:
                    current_module = {'num': '01', 'title': '1. Introduction to SQL & RDBMS', 'topics': []}
                # Subtopics might be multiple lines or comma-separated
                if line:
                    current_module['topics'].append(line)
                    
    if current_module:
        modules.append(current_module)
        
    return modules

# ==========================================
# 2. PARSE PYTHON DOCX
# ==========================================
def parse_python_docx(docx_path):
    doc = docx.Document(docx_path)
    raw_paras = [clean_text(p.text) for p in doc.paragraphs if clean_text(p.text)]
    
    modules = []
    current_module = None
    mod_pattern = re.compile(r'^(\d+)\.\s+(.*)')
    
    for p in raw_paras:
        p_lines = [l.strip() for l in p.split('\n') if l.strip()]
        for line in p_lines:
            if line.upper() == 'PYTHON':
                continue
            m = mod_pattern.match(line)
            is_main_mod = False
            if m and not re.match(r'^\d+\.\d+', line):
                is_main_mod = True
                
            if is_main_mod:
                if current_module:
                    modules.append(current_module)
                current_module = {
                    'num': m.group(1),
                    'title': line,
                    'topics': []
                }
            else:
                if current_module is None:
                    current_module = {'num': '01', 'title': '1. Introduction to Python & IDE', 'topics': []}
                if line:
                    current_module['topics'].append(line)
                    
    if current_module:
        modules.append(current_module)
    return modules

# ==========================================
# 3. PARSE COMBO (EXCEL + POWER BI + AI) DOCX
# ==========================================
def parse_combo_docx(docx_path):
    doc = docx.Document(docx_path)
    raw_paras = [clean_text(p.text) for p in doc.paragraphs if clean_text(p.text)]
    
    modules = []
    current_module = None
    
    # Module headers start with "MODULE 1:", "MODULE 2:", "MODULE 01 —", "PART I", "PART II", etc.
    mod_header_pattern = re.compile(r'^(MODULE\s+\d+|PART\s+[IVX]+)', re.IGNORECASE)
    
    for p in raw_paras:
        if p.startswith('•') or p.startswith('🎯') or p.startswith('1.') or p.startswith('2.') or p.startswith('3.'):
            # It's a topic/objective
            if current_module:
                cleaned = re.sub(r'^[•\s\-\*🎯]+', '', p).strip()
                if cleaned and len(cleaned) > 2:
                    current_module['topics'].append(cleaned)
        elif mod_header_pattern.match(p):
            if current_module:
                modules.append(current_module)
            current_module = {
                'num': str(len(modules) + 1),
                'title': p,
                'topics': []
            }
        else:
            # Check if it looks like a major section title
            if (p.isupper() and len(p) < 60) or ('Roadmap' in p) or ('Crash Course' in p):
                if current_module and len(current_module['topics']) > 0:
                    modules.append(current_module)
                    current_module = {
                        'num': str(len(modules) + 1),
                        'title': p,
                        'topics': []
                    }
            elif current_module:
                cleaned = re.sub(r'^[•\s\-\*]+', '', p).strip()
                if cleaned and len(cleaned) > 2:
                    current_module['topics'].append(cleaned)
                    
    if current_module:
        modules.append(current_module)
        
    # Filter out modules with 0 topics by merging them or cleaning
    filtered = []
    for m in modules:
        if len(m['topics']) > 0:
            filtered.append(m)
        elif filtered and len(m['topics']) == 0:
            # prepend title to next or append to previous
            pass
            
    return filtered

# ==========================================
# 4. PARSE MACHINE LEARNING DOCX
# ==========================================
def parse_ml_docx(docx_path):
    doc = docx.Document(docx_path)
    raw_paras = [clean_text(p.text) for p in doc.paragraphs if clean_text(p.text)]
    
    modules = []
    current_module = None
    mod_header_pattern = re.compile(r'^(MODULE\s+\d+|PART\s+[IVX]+)', re.IGNORECASE)
    
    for p in raw_paras:
        if mod_header_pattern.match(p):
            if current_module:
                modules.append(current_module)
            current_module = {
                'num': str(len(modules) + 1),
                'title': p,
                'topics': []
            }
        else:
            if current_module is None:
                current_module = {
                    'num': '1',
                    'title': 'MODULE 01 — Data Preparation, Preprocessing & Feature Engineering',
                    'topics': []
                }
            cleaned = re.sub(r'^[•\s\-\*]+', '', p).strip()
            if cleaned and len(cleaned) > 1 and not cleaned.startswith('Scope:'):
                current_module['topics'].append(cleaned)
                
    if current_module:
        modules.append(current_module)
        
    return [m for m in modules if len(m['topics']) > 0]

# ==========================================
# TEMPLATE GENERATOR
# ==========================================
def render_html(title, badge, duration, modules, out_path):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Detailed Syllabus Catalogue | NeoNex MindX</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=optional" rel="stylesheet">
  <style>
    :root {{
      --primary: #0F172A;
      --accent: #2563EB;
      --accent-light: #EFF6FF;
      --accent-border: #BFDBFE;
      --text: #1E293B;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --bg-alt: #F8FAFC;
      --success: #16A34A;
      --card-bg: #FFFFFF;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      color: var(--text);
      line-height: 1.6;
      background: #F1F5F9;
      padding: 40px 16px;
    }}
    .print-container {{
      max-width: 960px;
      margin: 0 auto;
      background: var(--card-bg);
      padding: 48px;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
      border: 1px solid var(--border);
    }}
    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 24px;
      border-bottom: 2px solid var(--accent-light);
      margin-bottom: 32px;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .brand-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand-logo-icon {{
      width: 36px;
      height: 36px;
      background: #EFF6FF;
      border: 1px solid #BFDBFE;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #2563EB;
    }}
    .badge {{
      display: inline-block;
      padding: 6px 14px;
      background: var(--accent-light);
      color: var(--accent);
      border: 1px solid var(--accent-border);
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .btn-print {{
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 10px 22px;
      border-radius: 10px;
      font-weight: 700;
      font-size: 14px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
    }}
    .btn-print:hover {{
      background: var(--accent);
      transform: translateY(-1px);
    }}
    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 32px;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 12px;
      line-height: 1.25;
      letter-spacing: -0.02em;
    }}
    .lead-desc {{
      font-size: 15.5px;
      color: var(--text-muted);
      margin-bottom: 32px;
      line-height: 1.6;
    }}
    .meta-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-bottom: 40px;
      background: var(--bg-alt);
      padding: 20px 24px;
      border-radius: 14px;
      border: 1px solid var(--border);
    }}
    .meta-item b {{
      color: var(--primary);
      display: block;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 4px;
    }}
    .meta-item span {{
      font-size: 15px;
      font-weight: 600;
      color: var(--text);
    }}
    .module-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 14px;
      margin-bottom: 24px;
      overflow: hidden;
      transition: all 0.2s;
    }}
    .module-card:hover {{
      border-color: #CBD5E1;
      box-shadow: 0 6px 20px rgba(15, 23, 42, 0.05);
    }}
    .module-header {{
      background: var(--bg-alt);
      padding: 18px 24px;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 14px;
      border-bottom: 1px solid var(--border);
    }}
    .module-number {{
      background: var(--accent);
      color: #ffffff;
      min-width: 30px;
      height: 30px;
      padding: 0 8px;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 700;
      flex-shrink: 0;
    }}
    .topic-list {{
      padding: 20px 24px;
      list-style: none;
      display: grid;
      gap: 10px;
    }}
    .topic-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 14.5px;
      color: var(--text);
      line-height: 1.5;
    }}
    .check-svg {{
      width: 17px;
      height: 17px;
      fill: none;
      stroke: var(--success);
      stroke-width: 2.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .subtopic-group {{
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 12px 16px;
      margin-top: 6px;
      font-size: 14px;
      color: #334155;
    }}
    @media (max-width: 768px) {{
      .print-container {{ padding: 24px 16px; }}
      h1 {{ font-size: 26px; }}
      .header-bar {{ flex-direction: column; align-items: flex-start; }}
    }}
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .print-container {{ border: none; box-shadow: none; padding: 0; max-width: 100%; }}
      .btn-print {{ display: none !important; }}
      .module-card {{ break-inside: avoid; page-break-inside: avoid; margin-bottom: 16px; }}
    }}
  </style>
</head>
<body>
  <div class="print-container">
    <div class="header-bar">
      <div class="brand-title">
        <div class="brand-logo-icon">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        NeoNex MindX
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <span class="badge">{badge}</span>
        <button class="btn-print" onclick="window.print()">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2M6 14h12v8H6z"/></svg>
          Download / Print PDF
        </button>
      </div>
    </div>

    <h1>{title}</h1>
    <p class="lead-desc">Official curriculum roadmap and modular breakdown designed for hands-on, industry-ready application with live project delivery.</p>

    <div class="meta-strip">
      <div class="meta-item">
        <b>Program Mode</b>
        <span>Live Interactive Online</span>
      </div>
      <div class="meta-item">
        <b>Curriculum Duration</b>
        <span>{duration}</span>
      </div>
      <div class="meta-item">
        <b>Certification</b>
        <span>NeoNex MindX Industry Certificate</span>
      </div>
      <div class="meta-item">
        <b>Support Line</b>
        <span>WhatsApp: +91 84318 03839</span>
      </div>
    </div>

    <div class="modules-container">
'''
    
    for i, m in enumerate(modules, 1):
        num_str = f"{i:02d}"
        html += f'''      <div class="module-card">
        <div class="module-header">
          <span class="module-number">{num_str}</span>
          <span>{m['title']}</span>
        </div>
        <ul class="topic-list">
'''
        for t in m['topics']:
            # If t contains newlines, split them
            lines = [l.strip() for l in t.split('\n') if l.strip()]
            for line in lines:
                html += f'''          <li class="topic-item">
            <svg class="check-svg" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>{line}</span>
          </li>
'''
        html += '''        </ul>
      </div>
'''
        
    html += '''    </div>
  </div>
</body>
</html>'''

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {out_path} ({len(modules)} modules)!")

# RUN GENERATIONS
sql_mods = parse_sql_docx("deployment_NeoNex/syllabus/individual modules/SQL  (3).docx")
render_html(
    title="SQL for Data Analytics & Engineering",
    badge="Short Course Syllabus",
    duration="4–6 Weeks",
    modules=sql_mods,
    out_path="deployment_NeoNex/syllabus/catalogues/sql-syllabus.html"
)

python_mods = parse_python_docx("deployment_NeoNex/syllabus/individual modules/Python (4).docx")
render_html(
    title="Python Programming for Beginners & Data Science",
    badge="Short Course Syllabus",
    duration="6–8 Weeks",
    modules=python_mods,
    out_path="deployment_NeoNex/syllabus/catalogues/python-programming-syllabus.html"
)

combo_mods = parse_combo_docx("c:/Users/pcnee/Downloads/COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx")
render_html(
    title="Excel, Power BI & Tableau Dashboard Course",
    badge="Short Course Syllabus",
    duration="7 Weeks",
    modules=combo_mods,
    out_path="deployment_NeoNex/syllabus/catalogues/excel-power-bi-tableau-syllabus.html"
)

ml_mods = parse_ml_docx("c:/Users/pcnee/Downloads/MACHINE LEARNING — COMPLETE ROADMAP (2).docx")
render_html(
    title="Machine Learning with Python",
    badge="Short Course Syllabus",
    duration="8–10 Weeks",
    modules=ml_mods,
    out_path="deployment_NeoNex/syllabus/catalogues/machine-learning-syllabus.html"
)
