import docx
import json
import re

# 1. Parse Excel Modules
doc_combo = docx.Document(r'C:\Users\pcnee\Downloads\COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx')
excel_modules = []
cur_mod = None

for p in doc_combo.paragraphs:
    t = p.text.strip()
    if not t: continue
    if t.startswith('MODULE ') and 'Excel' in t or (t.startswith('MODULE ') and any(w in t for w in ['Spreadsheet', 'Data Entry', 'Formulas', 'Referencing', 'Functions', 'Conditional', 'Text', 'Sorting', 'Pivot', 'Charts', 'Dashboarding', 'Power Query', 'VBA'])):
        if cur_mod:
            excel_modules.append(cur_mod)
        cur_mod = {'title': t, 'objective': '', 'topics': []}
    elif cur_mod:
        if t.startswith('🎯 Objective') or t == '🎯 Objective':
            continue
        elif not cur_mod['objective'] and not t[0].isdigit() and not t.startswith('•'):
            cur_mod['objective'] = t
        elif t[0].isdigit() and '.' in t[:4]:
            cur_mod['topics'].append(t)
        elif t.startswith('•') and cur_mod['topics']:
            sub = t.lstrip('• ').strip()
            cur_mod['topics'].append(f"  - {sub}")
        elif cur_mod['title'].startswith('MODULE 14') and 'VBA' in cur_mod['title'] and t == 'POWER BI':
            excel_modules.append(cur_mod)
            cur_mod = None
            break

if cur_mod:
    excel_modules.append(cur_mod)

print(f"Parsed {len(excel_modules)} Excel modules.")

# 2. Parse Power BI Section
pbi_modules = []
pbi_record = False
cur_pbi_mod = None

pbi_sections = [
    {"num": "15", "title": "Power BI Foundations, Architecture & Interface", "topics": ["What is Power BI & Components (Power Query, Power Pivot, Power View, Power BI Service)", "Power BI vs Tableau: Visualization Capabilities, Dataset Limits & Cost Comparison", "Installing & Updating Power BI Desktop & Preview Feature Setup", "Interface Layout: Fields Pane, Visualizations Pane, Filters Pane & Report Canvas", "Three Core Steps: Get Data, Choose Visualization, Select Fields"]},
    {"num": "16", "title": "Basic & Advanced Visualizations in Power BI", "topics": ["Column, Bar, Stacked Bar, Pie, Donut, Funnel, and Ribbon Charts", "Map Visualizations: Bubble Maps, Shape Maps, Filled Maps & India Regional Geo-Maps", "Tabular & Matrix Visuals: Hierarchies, Expand/Collapse & Conditional Formatting", "Time-Based Visuals: Line, Area, Stacked Area with Auto Date Hierarchies", "Advanced Visuals: 100% Stacked Bar, Decomposition Tree, Combo, Waterfall, Gauge & Treemap", "AppSource Marketplace Visuals: Animated Bar Chart Race, Word Cloud, Play Axis & Scroller"]},
    {"num": "17", "title": "Interactivity, Slicers, Bookmarks & Object Navigation", "topics": ["Number Cards, Multi-row Cards, Dynamic KPI Cards & Custom Metric Displays", "Filtering Architecture: Visual-level, Page-level, Report-level & Drill-down Filtering", "Slicers: Dynamic Text, Date Sliders, Range Sliders & Relative Time Slicers", "Shapes, Buttons, Action URLs & Web Integration", "Bookmarks & Selection Pane: Multi-view Interactive State Switching", "Drill-Through Navigation Pages & Contextual Tooltip Pages"]},
    {"num": "18", "title": "Power Query ETL & Data Engineering in Power BI", "topics": ["Power Query Editor: Ingestion, Extraction, Merging & Splitting Columns", "Text, Date & Numeric Transformations (Delimiter Parsing, Case Switching, Age Calc)", "Append & Merge Queries (Inner, Left Outer, Full Outer & Anti-Joins)", "Columns From Examples (CFE) & Conditional Columns (No-code IF/ELSE)", "Data Cleansing: Autofill, Fill Down/Up, Transpose, Unpivot Columns & Group By", "Synthetic Data Testing with Mockaroo Schema Modeling"]},
    {"num": "19", "title": "Data Modeling, Star Schema & DAX Foundations", "topics": ["Data View & Model View: Star Schema vs Snowflake Schema Architecture", "Relationship Cardinality: 1:1, 1:Many, Many:Many & Cross-Filter Direction Control", "Building Multi-Table Enterprise Models (Employee, Sales, Department, Financials)", "Calculated Columns vs Measures: Row Context vs Filter Context in VertiPaq Engine", "Core DAX Formulas: SUM, CALCULATE, FILTER, RELATED, ALLEXCEPT, DIVIDE, DATEDIFF", "Time Intelligence DAX: YTD, QTD, MTD, SAMEPERIODLASTYEAR & Growth Metrics"]},
    {"num": "20", "title": "Power BI Service, Cloud Dashboards & Enterprise Gateway", "topics": ["Publishing Reports to Power BI Cloud Service & Workspace Administration", "Building Executive Cloud Dashboards & Pinning Live Report Tiles", "Installing & Configuring On-Premises Data Gateway for Automated Cloud Refresh", "Scheduled Refresh Setup (Pro vs Premium Capacity) & Credential Troubleshooting", "Row-Level Security (RLS) Configuration, User Roles & Dashboard Subscriptions", "Connecting Power BI Directly to Live Relational SQL Server Databases"]}
]

# 3. Parse Tableau Stages from Tableau Docx
doc_tab = docx.Document(r'C:\Users\pcnee\Downloads\NeoNex_MindX_Tableau_Syllabus_Professional.docx')
tableau_modules = [
    {"num": "21", "title": "Tableau Foundations, Products & Workflow", "desc": "Stage 01: Connect to diverse enterprise data sources and master core visual analytics.", "topics": ["What is Tableau & Architectural Capabilities (50+ Sources, 24 Native Charts)", "Tableau Product Suite: Desktop, Public, Online, Server, Reader & Tableau Prep", "Basic Workflow: Connecting Data, Dimensions vs Measures, Discrete vs Continuous (Blue vs Green Pills)", "Tableau vs Excel Analytical Paradigm Differences & Data Extraction Methods"]},
    {"num": "22", "title": "Data Organization, Sorting & Visual Formatting", "desc": "Stage 02 & 03: Column operations, hierarchies, custom groups, and sheet layout.", "topics": ["Column Operations, Granularity, Aliasing, Renaming & Data Type Formatting", "Row & Graph Sorting (Computed, Manual, Nested & Hierarchical Sorts)", "Custom Groups, Sets & Hierarchies (Drill-down Dimensions)", "Formatting Worksheets, Custom Color Palettes, Shapes, Dynamic Labels & Titles", "Exporting Worksheets & Dashboards to PDF, PowerPoint, Image & Packaged Workbooks"]},
    {"num": "23", "title": "Calculations, Table Calcs & Level of Detail (LOD) Expressions", "desc": "Stage 04: Advanced analytical formulas, parameter controls, and deep metrics.", "topics": ["Basic Calculated Fields: String, Date, Logical (IF-THEN, CASE) & Number Functions", "Table Calculations: Running Total, Difference, % Difference, % of Total & Rank", "Level of Detail (LOD) Expressions: FIXED, INCLUDE & EXCLUDE Calculations", "Interactive Dynamic Parameters: What-If Analysis, Top N Dynamic Dimension Switches", "Reference Lines, Bands, Distributions & Box Plots for Statistical Dispersion"]},
    {"num": "24", "title": "Interactive Dashboards, Storytelling & SQL Integration", "desc": "Stage 05, 06 & 07: Professional enterprise dashboards, forecasting, and live database feeds.", "topics": ["Dashboard Layout & Design: Tiled vs Floating Containers, Device Preview Mode", "Dashboard Action Filters: Filter, Highlight, Go to URL & Change Parameter Actions", "Story Points & Data Storytelling for Executive Presentations", "Advanced Visuals: Dual Axis Charts, Donut Charts, Waterfall & Pareto Analysis", "Analytics Pane: Trend Lines, Forecasting, Clustering & Summary Statistics", "Connecting Tableau Directly to SQL Server & Custom SQL Query Modeling"]}
]

print("Structures ready for comprehensive curriculum generation.")
