import glob

files = [
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    has_download = 'download' in txt.lower() and 'syllabus' in txt.lower()
    print(f, "has download syllabus:", has_download)
