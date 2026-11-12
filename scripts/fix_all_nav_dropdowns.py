import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
count = 0
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        # Look for short course dropdown hrefs
        new_content = content
        # Check /courses/excel-power-bi-tableau-course without slash
        new_content = re.sub(r'href=["\']/courses/excel-power-bi-tableau-course["\']', 'href="/courses/excel-power-bi-tableau-course/"', new_content)
        new_content = re.sub(r'href=["\']/courses/sql-course["\']', 'href="/courses/sql-course/"', new_content)
        new_content = re.sub(r'href=["\']/courses/python-programming-course["\']', 'href="/courses/python-programming-course/"', new_content)
        new_content = re.sub(r'href=["\']/courses/machine-learning-course["\']', 'href="/courses/machine-learning-course/"', new_content)
        
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            count += 1
    except Exception as e:
        pass

print(f"Updated dropdown links to have trailing slash in {count} HTML files.")
