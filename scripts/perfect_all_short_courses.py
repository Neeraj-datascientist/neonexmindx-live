import re
import glob

paths = [
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

short_meta = {
    'python-programming-course': {
        'eyebrow': '18-module complete curriculum',
        'count': 18,
        'title': 'Python Programming Course Online in India | NeoNex MindX',
        'h1': 'Live Online Python Programming Course for Beginners in India',
        'desc': 'Join a live Python programming course online in India covering coding foundations, OOP, file handling, NumPy, Pandas, EDA and practical projects.'
    },
    'sql-course': {
        'eyebrow': '22-module complete curriculum',
        'count': 22,
        'title': 'SQL Course Online in India with Real Database Projects | NeoNex MindX',
        'h1': 'Live Online SQL Course in India with Real Database Projects',
        'desc': 'Join a live SQL course online in India covering relational databases, CRUD, joins, subqueries, CTEs, views, window functions, procedures, transactions & projects.'
    },
    'excel-power-bi-tableau-course': {
        'eyebrow': '24-module complete curriculum',
        'count': 24,
        'title': 'Excel, Power BI & Tableau Course Online in India | NeoNex MindX',
        'h1': 'Excel, Power BI & Tableau Course Online in India',
        'desc': 'Master Excel, Power BI & Tableau in India. Hands-on course covering formulas, macros, Power Query ETL, Star Schema data modeling, DAX, LOD calculations & dashboards.'
    },
    'machine-learning-course': {
        'eyebrow': '9-module complete curriculum',
        'count': 9,
        'title': 'Machine Learning Course Online in India with Python | NeoNex MindX',
        'h1': 'Machine Learning Course Online in India with Python',
        'desc': 'Join an applied Machine Learning course online in India covering feature engineering, supervised regression, clustering, PCA, model validation, tuning & deployment.'
    }
}

for path in paths:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = [k for k in short_meta if k in path][0]
    meta = short_meta[slug]

    # 1. Trailing slashes on internal career program and short course links
    career_slugs = [
        'data-science-course', 'data-analytics-course', 'data-engineering-course',
        'business-analytics-course', 'ai-ml-course', 'ai-ml-engineering-course',
        'generative-ai-engineering-course', 'python-programming-course',
        'sql-course', 'excel-power-bi-tableau-course', 'machine-learning-course'
    ]
    for cs in career_slugs:
        html = re.sub(f'href=["\']/courses/{cs}["\']', f'href="/courses/{cs}/"', html)

    # 2. Synchronize Eyebrow claim with actual module count
    html = re.sub(r'<p class="eyebrow">\s*\d+-module.*?</p>', f'<p class="eyebrow">{meta["eyebrow"]}</p>', html, flags=re.I)
    html = re.sub(r'\b\d+\s+modules\b', f'{meta["count"]} modules', html, flags=re.I)

    # 3. Ensure high-intent H1 tag has zero layout shift
    # Inject high-intent H1 keyword cleanly
    if f'<h1 class="eyebrow"' not in html:
        # replace the hero-title eyebrow or insert before hero-title
        if '<span class="eyebrow">' in html:
            html = html.replace('<span class="eyebrow">', f'<h1 class="eyebrow" style="font-size:0.95rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--brand-primary,#0056D2);margin-bottom:8px;font-weight:700;">{meta["h1"]}</h1><!-- ', 1)
            html = html.replace('</span>', ' -->', 1)
        elif '<p class="eyebrow">' in html:
            # check if hero eyebrow
            hero_eyebrow = html.find('class="eyebrow"')
            html = html[:hero_eyebrow-3] + f'<h1 class="eyebrow" style="font-size:0.95rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--brand-primary,#0056D2);margin-bottom:8px;font-weight:700;">{meta["h1"]}</h1>\n' + html[hero_eyebrow-3:]

    # 4. Standardize meta description length and content
    html = re.sub(r'<meta name="description" content=".*?"\s*>', f'<meta name="description" content="{meta["desc"]}">', html)
    html = re.sub(r'<meta content=".*?" name="description"\s*>', f'<meta content="{meta["desc"]}" name="description">', html)

    # 5. Fix any placeholder emails
    html = html.replace('you@example.com', 'yourname@email.com')
    html = html.replace('name@example.com', 'yourname@email.com')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Calibrated {path} to perfection.")
