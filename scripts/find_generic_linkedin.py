import re

files = [
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html',
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/data-science-course/index.html',
    'deployment_NeoNex/courses/data-science-and-ai-course/index.html',
    'deployment_NeoNex/courses/data-analytics-course/index.html',
    'deployment_NeoNex/courses/ai-ml-course/index.html',
    'deployment_NeoNex/courses/business-analytics-course/index.html',
    'deployment_NeoNex/courses/data-engineering-course/index.html',
    'deployment_NeoNex/courses/generative-ai-engineering-course/index.html',
]

for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    # find where linkedin.com/ is used
    matches = re.findall(r'href=[\"\']https://www\.linkedin\.com/?[\"\']', txt)
    if matches:
        print(f"{f}: {len(matches)} generic linkedin links")
        # print context
        for m in re.finditer(r'.{0,100}https://www\.linkedin\.com/?.{0,100}', txt):
            if 'company' not in m.group(0) and '/in/' not in m.group(0) and 'share-offsite' not in m.group(0):
                print("  Context:", m.group(0).replace('\n', ' '))
