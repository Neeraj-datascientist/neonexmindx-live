import docx
import re
import os
import shutil

# 1. Parse Excel Modules (14 modules)
doc_combo = docx.Document(r'C:\Users\pcnee\Downloads\COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx')
excel_modules = []
cur_mod = None

for p in doc_combo.paragraphs:
    t = p.text.strip()
    if not t: continue
    if t.startswith('MODULE ') and ('Excel' in t or any(w in t for w in ['Spreadsheet', 'Data Entry', 'Formulas', 'Referencing', 'Functions', 'Conditional', 'Text', 'Sorting', 'Pivot', 'Charts', 'Dashboarding', 'Power Query', 'VBA'])):
        if cur_mod:
            excel_modules.append(cur_mod)
        clean_title = re.sub(r'^MODULE\s+\d+:\s*', '', t).strip()
        num_str = re.search(r'\d+', t)
        n = int(num_str.group()) if num_str else len(excel_modules)+1
        cur_mod = {'num': f"{n:02d}", 'title': clean_title, 'objective': '', 'topics': []}
    elif cur_mod:
        if t.startswith('🎯 Objective') or t == '🎯 Objective':
            continue
        elif not cur_mod['objective'] and not t[0].isdigit() and not t.startswith('•'):
            cur_mod['objective'] = t
        elif t[0].isdigit() and '.' in t[:4]:
            topic_clean = re.sub(r'^\d+\.\d+\s*', '', t).strip()
            cur_mod['topics'].append(topic_clean)
        elif cur_mod['title'].startswith('VBA') and t == 'POWER BI':
            excel_modules.append(cur_mod)
            cur_mod = None
            break

if cur_mod and cur_mod not in excel_modules:
    excel_modules.append(cur_mod)

print(f"Parsed {len(excel_modules)} Excel modules.")

# 2. Power BI Modules (6 comprehensive modules mapped from 27 sections)
pbi_modules = [
    {
        "num": "15",
        "title": "Power BI Architecture, Installation & Core Interface",
        "objective": "Understand the Power BI ecosystem, compare features against Tableau, and master the report development canvas.",
        "topics": [
            "What is Power BI & Core Architecture (Desktop, Service, Mobile, Report Server)",
            "Components: Power Query (ETL), Power Pivot (Modeling), Power View (Visuals) & Service (Sharing)",
            "Power BI vs Tableau: Visual Capabilities, Dataset Size Limits & Cost Comparison",
            "Installing & Updating Power BI Desktop & Configuring Preview Features",
            "Interface Architecture: Fields Pane, Visualizations Pane, Filters Pane & Report Canvas",
            "The Three Core Steps in Power BI: Get Data, Choose Visualization, Select Fields"
        ]
    },
    {
        "num": "16",
        "title": "Comprehensive Visual Analytics & Custom Visuals",
        "objective": "Build executive-grade visuals from standard bar/line charts to geospatial maps and AppSource marketplace extensions.",
        "topics": [
            "Standard Visuals: Column, Bar, Stacked Bar, Pie, Donut, Funnel & Ribbon Charts",
            "Geospatial Visualizations: Bubble Maps, Filled Maps, Shape Maps & Custom Regional India Maps",
            "Tabular & Hierarchical Visuals: Table & Matrix with Expand/Collapse & Conditional Formatting (Icons, Heatmaps)",
            "Time-Series Visuals: Line Chart, Area Chart, Stacked Area Chart with Auto Date Hierarchies (Year > Quarter > Month > Day)",
            "Advanced Analytical Visuals: Decomposition Tree, Waterfall Chart, Combo Charts, Gauge & Treemap",
            "AppSource Marketplace Visuals: Animated Bar Chart Race, Word Cloud, Infographic Visual, Play Axis & Scroller"
        ]
    },
    {
        "num": "17",
        "title": "Report Interactivity, Slicers, Bookmarks & Navigation",
        "objective": "Design dynamic, user-friendly business applications with interactive state switching and drill-down controls.",
        "topics": [
            "KPI Cards: Single-Value Cards, Multi-row Cards, Dynamic KPI Metrics & Card Formatting",
            "Hierarchical Filtering: Visual-Level, Page-Level, Report-Level & Drill-Down Filtering",
            "Dynamic Slicers: Text Slicers, Date Sliders, Relative Date Slicers & Dropdown Numeric Slicers",
            "Inserting Interactive Objects: Shapes, Image Placeholders, Buttons & Action Web URLs",
            "Bookmarks & Selection Pane: Building Pop-up Filter Panes and Multi-view Viewports",
            "Page Navigation & Drill-Through: Creating Contextual Detail Pages and Hover Tooltip Pages"
        ]
    },
    {
        "num": "18",
        "title": "Power Query ETL & Data Engineering in Power BI",
        "objective": "Master data extraction, transformation, and automated loading pipelines directly inside Power Query.",
        "topics": [
            "Power Query Editor Interface & Architecture: Ingesting Excel, CSV, Web, Folders & Databases",
            "Text, Date & Numeric Transformations: Delimiters, Case Formatting, Extract, Age, Duration & Math Rounding",
            "Append Queries (Union) & Merge Queries (Joins: Inner, Left Outer, Right, Full Outer & Anti-Joins)",
            "Columns From Example (CFE / Flash Fill) & Conditional Columns (No-Code IF/ELSE Logic)",
            "Data Cleansing: Autofill, Fill Down/Up, Transpose, Unpivot Columns & Group By Aggregations",
            "Synthetic Data Modeling & Schema Testing using Mockaroo Data Generation"
        ]
    },
    {
        "num": "19",
        "title": "Data Modeling, Star Schema & DAX Formulas",
        "objective": "Architect enterprise star schemas and write high-performance DAX measures for real-time KPI reporting.",
        "topics": [
            "Data View & Model View: Star Schema vs Snowflake Schema Architecture",
            "Relationship Cardinality: 1-to-Many, Many-to-Many & Active vs Inactive Relationships",
            "Multi-Table Enterprise Modeling (Sales, Customer, Product, Department, Financial Targets)",
            "Calculated Columns vs Measures: Row Context vs Filter Context in the VertiPaq Engine",
            "Core DAX Aggregations: SUM, AVERAGE, COUNT, DIVIDE, RELATED, RELATEDTABLE",
            "Advanced DAX & Filter Modification: CALCULATE, FILTER, ALL, ALLEXCEPT, KEEPFILTERS",
            "Time Intelligence DAX: YTD, QTD, MTD, SAMEPERIODLASTYEAR, DATEADD & Moving Averages"
        ]
    },
    {
        "num": "20",
        "title": "Power BI Service, Cloud Dashboards, Gateways & Security",
        "objective": "Deploy reports to the cloud, configure automated data refresh gateways, and secure corporate datasets.",
        "topics": [
            "Publishing Reports to Power BI Cloud Service & Workspace Role Management (Admin, Member, Viewer)",
            "Building Executive Cloud Dashboards & Pinning Live Report Visuals",
            "Installing & Configuring On-Premises Data Gateway for Local Network & SQL Server Refresh",
            "Scheduled Refresh Setup (Pro 8x/day vs Premium 48x/day) & Resolving Credential Failures",
            "Row-Level Security (RLS): Defining DAX Roles, Testing Security as User & Production Deployment",
            "DirectQuery vs Import Mode & Connecting Power BI to Live Relational SQL Server Databases"
        ]
    }
]

# 3. Tableau Modules (4 comprehensive modules mapped from 7 stages)
tableau_modules = [
    {
        "num": "21",
        "title": "Tableau Foundations, Architecture & Workflow",
        "objective": "Understand Tableau's visual engine, product ecosystem, and foundational data preparation workflow.",
        "topics": [
            "Introduction to Tableau & Capabilities (50+ Data Connectors, 24 Native Visualizations)",
            "Tableau Product Suite: Desktop, Public, Server, Cloud/Online, Reader & Tableau Prep Builder",
            "Core Visual Workflow: Connecting to Data, Dimensions vs Measures, Discrete vs Continuous (Blue vs Green Pills)",
            "Sample Superstore Dataset Walkthrough & Basic Chart Creation (Bar, Line, Scatter, Highlight Tables)",
            "Tableau vs Excel Paradigm Comparison: Granularity, Aggregation Levels & In-Memory Hyper Engine"
        ]
    },
    {
        "num": "22",
        "title": "Data Organization, Sorting, Sets & Visual Design",
        "objective": "Structure complex datasets with hierarchies, custom sets, color encoding, and presentation formatting.",
        "topics": [
            "Column Operations: Granularity, Renaming, Aliasing, Data Types, Copying & Default Properties",
            "Row & Graph Sorting: Manual, Computed, Nested & Hierarchical Multi-Field Sorting",
            "Custom Groups & Sets: Dynamic In/Out Sets, Combined Sets & Drill-down Hierarchies",
            "Formatting Worksheets: Custom Color Palettes, Font Sizing, Cell Borders, Tooltips & Dynamic Labels",
            "Exporting Visuals & Workbooks: Exporting to PDF, PowerPoint, Image, Excel Data & Packaged (.twbx) Workbooks"
        ]
    },
    {
        "num": "23",
        "title": "Calculated Fields, Table Calcs & Level of Detail (LOD)",
        "objective": "Perform sophisticated statistical modeling, advanced table calculations, and LOD expressions.",
        "topics": [
            "Calculated Fields: String Functions, Date Manipulations, Number Functions & Logical (IF-THEN, CASE)",
            "Table Calculations: Running Total, Difference, % Difference, % of Total, Rank & Moving Averages",
            "Level of Detail (LOD) Expressions: FIXED (Independent of View), INCLUDE (Finer Grain) & EXCLUDE (Coarser Grain)",
            "Dynamic Parameters: What-If Analysis, Top N Dimension Filtering & Metric Switching Controls",
            "Statistical Reference Lines, Reference Bands, Box Plots, Distributions & Trend Line Modeling"
        ]
    },
    {
        "num": "24",
        "title": "Interactive Dashboards, Story Points & SQL Connectivity",
        "objective": "Design production-grade executive dashboards with dynamic actions, forecasting, and live SQL databases.",
        "topics": [
            "Dashboard Architecture: Tiled vs Floating Containers, Grid Alignment & Device Preview Layouts",
            "Dashboard Interactivity: Filter Actions, Highlight Actions, Go to URL & Parameter Update Actions",
            "Story Points: Crafting Executive Data Stories with Guided Annotations and Narrative Flow",
            "Advanced Visualizations: Dual Axis Charts, Donut Charts, Waterfall Charts & Pareto 80/20 Analysis",
            "Analytics Pane: Time-Series Forecasting, K-Means Clustering & Summary Statistics",
            "Connecting Tableau to Live SQL Server: Custom SQL Queries, Table Joins, Data Extracts & Cloud Publishing"
        ]
    }
]

all_modules = excel_modules + pbi_modules + tableau_modules
print(f"Total modules: {len(all_modules)}")

# Generate 2-Column Grid HTML with Clean Green Checks and Sleek White Cards
cards_html = []
for i, m in enumerate(all_modules):
    n = m['num']
    title = m['title']
    topics = m.get('topics', [])
    
    # Render topics with green checkmarks exactly as in user screenshot
    topics_list = "".join([f'''<li style="display:flex;align-items:flex-start;gap:10px;margin-bottom:9px;font-size:13.5px;color:#334155;line-height:1.45;">
      <svg style="width:16px;height:16px;min-width:16px;color:#16a34a;margin-top:2px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      <span>{t}</span>
    </li>''' for t in topics])

    open_attr = " open" if i in [0, 2] else ""  # First module in each col open for preview
    
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

# Split into 2 columns for high-end desktop presentation
col1_cards = "\n".join(cards_html[0::2])
col2_cards = "\n".join(cards_html[1::2])

curriculum_container = f'''
<div class="course-modules-toolbar" style="display:flex;justify-content:space-between;align-items:center;background:#f8fafc;border:1px solid #e2e8f0;padding:12px 18px;border-radius:12px;margin:20px 0 20px;flex-wrap:wrap;gap:10px;">
  <span style="font-size:13.5px;color:#334155;font-weight:600;">Course Modules &amp; Topics: <strong style="color:#0f172a;">Complete 24-Module Master Catalog</strong></span>
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

# Now inject into index.html of excel course
target_file = r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html'
with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace curriculum section contents
start_pos = html.find('<div class="curriculum">')
if start_pos == -1:
    start_pos = html.find('<div class="curriculum-wrapper">')
if start_pos == -1:
    start_pos = html.find('<div class="curriculum-grid-2col">')
if start_pos == -1:
    start_pos = html.find('id="curriculum"')
    phase_end = html.find('</div></div>', start_pos)
    start_pos = phase_end + 12

# Find end before next section
end_pos = html.find('</div>\n</div>\n</section>', start_pos)
if end_pos == -1:
    end_pos = html.find('</div></div></section>', start_pos)
if end_pos == -1:
    end_pos = html.find('</section>', start_pos)
    sub = html[start_pos:end_pos]
    last_div = sub.rfind('</div>')
    end_pos = start_pos + last_div

html = html[:start_pos] + '\n<div class="curriculum-wrapper">\n' + curriculum_container + '\n</div>\n' + html[end_pos:]

# Add rotate style for details open
if '.curriculum-grid-2col details[open] .plus' not in html:
    style_inject = '''<style>
.curriculum-grid-2col details[open] .plus { transform: rotate(45deg); display: inline-block; color: #dc2626 !important; }
.curriculum-grid-2col details summary::-webkit-details-marker { display:none; }
.curriculum-grid-2col details summary::marker { display:none; }
.curriculum-grid-2col details[open] { border-color: #bfdbfe !important; box-shadow: 0 4px 14px rgba(37,99,235,0.06) !important; }
</style>'''
    html = html.replace('</head>', style_inject + '\n</head>')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html)

# Also sync to finalised_deployment
dst_file = r'c:\Users\pcnee\Desktop\NeoNeX MindX website\finalised_deployment\courses\excel-power-bi-tableau-course\index.html'
os.makedirs(os.path.dirname(dst_file), exist_ok=True)
shutil.copy2(target_file, dst_file)

print("Excel, Power BI & Tableau page successfully updated with 2-column screenshot-accurate curriculum layout!")
