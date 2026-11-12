import docx
import re
import os

def build_syllabus_catalogue(title, badge, duration, docx_path, out_html_path):
    doc = docx.Document(docx_path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Detailed Syllabus Catalogue | NeoNex MindX</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=optional" rel="stylesheet">
  <style>
    :root {{
      --primary: #102a43;
      --accent: #2563eb;
      --accent-light: #eff6ff;
      --text: #1f2937;
      --text-muted: #4b5563;
      --border: #e2e8f0;
      --bg-alt: #f8fafc;
      --success: #16a34a;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      color: var(--text);
      line-height: 1.6;
      background: #f1f5f9;
      padding: 32px 16px;
    }}
    .print-container {{
      max-width: 920px;
      margin: 0 auto;
      background: #ffffff;
      padding: 48px;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(16,42,67,0.06);
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
      gap: 10px;
    }}
    .badge {{
      display: inline-block;
      padding: 6px 14px;
      background: var(--accent-light);
      color: var(--accent);
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
      padding: 10px 20px;
      border-radius: 10px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .btn-print:hover {{
      background: var(--accent);
    }}
    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 32px;
      color: var(--primary);
      margin-bottom: 12px;
      line-height: 1.25;
    }}
    .lead-desc {{
      font-size: 16px;
      color: var(--text-muted);
      margin-bottom: 32px;
      line-height: 1.6;
    }}
    .meta-strip {{
      display: flex;
      gap: 20px;
      margin-bottom: 40px;
      background: var(--bg-alt);
      padding: 16px 20px;
      border-radius: 12px;
      border: 1px solid var(--border);
      flex-wrap: wrap;
    }}
    .meta-item b {{
      color: var(--primary);
      display: block;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
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
      margin-bottom: 20px;
      overflow: hidden;
      transition: box-shadow 0.2s;
    }}
    .module-card:hover {{
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    }}
    .module-header {{
      background: var(--bg-alt);
      padding: 16px 20px;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .module-number {{
      background: var(--accent);
      color: #ffffff;
      width: 28px;
      height: 28px;
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
    }}
    .topic-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
      font-size: 14.5px;
      color: var(--text);
      line-height: 1.5;
    }}
    .topic-item:last-child {{
      margin-bottom: 0;
    }}
    .check-svg {{
      width: 16px;
      height: 16px;
      fill: none;
      stroke: var(--success);
      stroke-width: 2.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      flex-shrink: 0;
      margin-top: 3px;
    }}
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .print-container {{ border: none; box-shadow: none; padding: 0; }}
      .btn-print {{ display: none !important; }}
    }}
  </style>
</head>
<body>
  <div class="print-container">
    <div class="header-bar">
      <div class="brand-title">
        <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#2563eb" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        NeoNex MindX
      </div>
      <div>
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
    
    # Parse docx paragraphs into modules
    current_module = None
    modules = []
    
    for p in paras:
        p_clean = p.strip()
        if not p_clean: continue
        # Detect Module heading
        if p_clean.lower().startswith('module') or re.match(r'^\d+\.\s+[A-Z]', p_clean) or p_clean.isupper() and len(p_clean) < 60:
            if current_module:
                modules.append(current_module)
            current_module = {'title': p_clean, 'topics': []}
        else:
            if current_module is None:
                current_module = {'title': 'Course Foundations', 'topics': []}
            current_module['topics'].append(p_clean)
            
    if current_module:
        modules.append(current_module)
        
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
            html += f'''          <li class="topic-item">
            <svg class="check-svg" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>{t}</span>
          </li>
'''
        html += '''        </ul>
      </div>
'''
        
    html += '''    </div>
  </div>
</body>
</html>'''

    os.makedirs(os.path.dirname(out_html_path), exist_ok=True)
    with open(out_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {out_html_path} successfully ({len(modules)} modules)!")

# 1. SQL Course Syllabus
build_syllabus_catalogue(
    title="SQL for Data Analytics & Engineering",
    badge="Short Course Syllabus",
    duration="4–6 Weeks",
    docx_path="deployment_NeoNex/syllabus/individual modules/SQL  (3).docx",
    out_html_path="deployment_NeoNex/syllabus/catalogues/sql-syllabus.html"
)

# 2. Python Programming Course Syllabus
build_syllabus_catalogue(
    title="Python Programming for Beginners & Data Science",
    badge="Short Course Syllabus",
    duration="6–8 Weeks",
    docx_path="deployment_NeoNex/syllabus/individual modules/Python (4).docx",
    out_html_path="deployment_NeoNex/syllabus/catalogues/python-programming-syllabus.html"
)

# 3. Excel, Power BI & Tableau Course Syllabus
build_syllabus_catalogue(
    title="Excel, Power BI & Tableau Dashboard Course",
    badge="Short Course Syllabus",
    duration="7 Weeks",
    docx_path="c:/Users/pcnee/Downloads/COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx",
    out_html_path="deployment_NeoNex/syllabus/catalogues/excel-power-bi-tableau-syllabus.html"
)

# 4. Machine Learning Course Syllabus
build_syllabus_catalogue(
    title="Machine Learning with Python",
    badge="Short Course Syllabus",
    duration="8–10 Weeks",
    docx_path="c:/Users/pcnee/Downloads/MACHINE LEARNING — COMPLETE ROADMAP (2).docx",
    out_html_path="deployment_NeoNex/syllabus/catalogues/machine-learning-syllabus.html"
)

