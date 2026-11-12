import re

paths = [
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

meta_map = {
    'python-programming-course': 'Join a live Python programming course online in India covering coding foundations, OOP, file handling, NumPy, Pandas, EDA and practical projects.',
    'sql-course': 'Join a live SQL course online in India covering relational databases, CRUD, joins, subqueries, CTEs, views, window functions, procedures, transactions & projects.',
    'excel-power-bi-tableau-course': 'Master Excel, Power BI & Tableau in India. Hands-on course covering formulas, macros, Power Query ETL, Star Schema data modeling, DAX, LOD calculations & dashboards.',
    'machine-learning-course': 'Join an applied Machine Learning course online in India covering feature engineering, supervised regression, clustering, PCA, model validation, tuning & deployment.'
}

for path in paths:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = [k for k in meta_map if k in path][0]
    desc = meta_map[slug]

    # Remove existing meta description tag if any
    html = re.sub(r'<meta[^>]*name=["\']description["\'][^>]*>', '', html, flags=re.I)
    html = re.sub(r'<meta[^>]*content=["\'][^"\']*["\'][^>]*name=["\']description["\'][^>]*>', '', html, flags=re.I)

    # Insert clean standard meta description right after title
    title_pos = html.find('</title>')
    if title_pos != -1:
        insert_str = f'\n<meta name="description" content="{desc}">'
        html = html[:title_pos+8] + insert_str + html[title_pos+8:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Cleaned meta description in {path}")
