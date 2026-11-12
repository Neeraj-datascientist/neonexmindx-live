import re

files = [
    'courses/sql-course/index.html',
    'courses/python-programming-course/index.html',
    'courses/excel-power-bi-tableau-course/index.html',
    'courses/machine-learning-course/index.html'
]

for f in files:
    path = 'deployment_NeoNex/' + f
    txt = open(path, 'r', encoding='utf-8').read()
    
    # Check if there is floating whatsapp or whatsapp widget
    floating = 'floating' in txt.lower() or 'wa-float' in txt.lower() or 'whatsapp-float' in txt.lower()
    print(f, "has floating WA:", floating)

