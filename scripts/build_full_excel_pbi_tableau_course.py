import docx
import re
import os
import shutil

# 1. Parse Excel Modules
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

print(f"Extracted {len(excel_modules)} Excel modules.")

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

# 3. Tableau Modules (4 comprehensive modules mapped from all 7 stages)
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
print(f"Total Combined Modules: {len(all_modules)} (14 Excel + 6 Power BI + 4 Tableau)")

# Generate HTML for Curriculum
html_modules = []
for i, m in enumerate(all_modules):
    open_attr = " open" if i == 0 else ""
    n = m['num']
    title = m['title']
    obj = m.get('objective', '')
    topics_list = m.get('topics', [])
    
    topics_html = "".join([f'<li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg><span>{t}</span></li>' for t in topics_list])
    
    mod_html = f'''<details class="module"{open_attr}>
  <summary><span class="module-number">{n}</span><span><b>{title}</b>{f"<small>{obj}</small>" if obj else ""}</span><span class="module-toggle" aria-hidden="true">+</span></summary>
  <div class="module-body"><ul>{topics_html}</ul></div>
</details>'''
    html_modules.append(mod_html)

curriculum_inner = "\n".join(html_modules)

# Update the HTML file
html_file_path = r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html'
with open(html_file_path, 'r', encoding='utf-8') as f:
    full_html = f.read()

# Update eyebrow
full_html = re.sub(r'<p class="eyebrow">\s*\d+-module curriculum\s*</p>', '<p class="eyebrow">24-module complete curriculum</p>', full_html)
full_html = re.sub(r'12 modules', '24 comprehensive modules', full_html)
full_html = re.sub(r'12-module curriculum', '24-module complete curriculum', full_html)

# Update phase grid
old_phase_grid = re.search(r'<div class="phase-grid">.*?</div></div>', full_html, re.DOTALL)
new_phase_grid = '''<div class="phase-grid">
  <div class="phase"><b>Phase 1 &middot; Excel Master (14 Modules)</b><span>Spreadsheet design, formulas, logic, lookup models, data cleaning, PivotTables, dashboarding, Power Query ETL & VBA macros.</span></div>
  <div class="phase"><b>Phase 2 &middot; Power BI Intelligence (6 Modules)</b><span>Data connections, custom visuals, interactive bookmarks, slicers, Star Schema modeling, enterprise DAX, Gateway & Cloud Service.</span></div>
  <div class="phase"><b>Phase 3 &middot; Tableau Storytelling (4 Modules)</b><span>Visual analytics, custom sets, Level of Detail (LOD) expressions, parameters, dynamic action dashboards & SQL integration.</span></div>
  <div class="phase"><b>Phase 4 &middot; Real-World Capstones & Certification</b><span>3 industry-standard portfolio capstone dashboards across Excel, Power BI and Tableau with interview preparation.</span></div>
</div>'''

if old_phase_grid:
    full_html = full_html[:old_phase_grid.start()] + new_phase_grid + full_html[old_phase_grid.end():]

# Replace the curriculum accordion items
curr_start = full_html.find('<div class="curriculum">')
if curr_start != -1:
    # Find next section or closing tag
    curr_end = full_html.find('</div></div></section>', curr_start)
    if curr_end == -1:
        curr_end = full_html.find('</div>\n</div>\n</section>', curr_start)
    if curr_end == -1:
        # fallback: find next section
        curr_end = full_html.find('</section>', curr_start)
        # backtrack to last </div> before </section>
        sub = full_html[curr_start:curr_end]
        last_div = sub.rfind('</div>')
        curr_end = curr_start + last_div

    full_html = full_html[:curr_start + len('<div class="curriculum">')] + "\n" + curriculum_inner + "\n" + full_html[curr_end:]
    print("Curriculum successfully injected into HTML!")
else:
    print("Could not find <div class=\"curriculum\">!")

# Update canonical and meta description
full_html = re.sub(r'rel="canonical" href="https://neonexmindx\.com/courses/excel-power-bi-tableau-course.*?"', 'rel="canonical" href="https://neonexmindx.com/courses/excel-power-bi-tableau-course/"', full_html)
full_html = full_html.replace('alt="" src="https://www.facebook.com/tr?id=1698036971288322', 'alt="Facebook Pixel" src="https://www.facebook.com/tr?id=1698036971288322')

with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

# Also sync to finalised_deployment
dst_file = r'c:\Users\pcnee\Desktop\NeoNeX MindX website\finalised_deployment\courses\excel-power-bi-tableau-course\index.html'
os.makedirs(os.path.dirname(dst_file), exist_ok=True)
shutil.copy2(html_file_path, dst_file)
print("Saved to deployment_NeoNex and mirrored to finalised_deployment.")

