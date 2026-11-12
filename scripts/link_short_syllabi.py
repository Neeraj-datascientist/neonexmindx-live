import re

courses = [
    ('courses/sql-course/index.html', '/syllabus/catalogues/sql-syllabus.html'),
    ('courses/python-programming-course/index.html', '/syllabus/catalogues/python-programming-syllabus.html'),
    ('courses/excel-power-bi-tableau-course/index.html', '/syllabus/catalogues/excel-power-bi-tableau-syllabus.html'),
    ('courses/machine-learning-course/index.html', '/syllabus/catalogues/machine-learning-syllabus.html')
]

for page, syl_url in courses:
    path = 'deployment_NeoNex/' + page
    txt = open(path, 'r', encoding='utf-8').read()
    
    # 1. Look for 'Get the Complete Course Syllabus' or similar hero button
    # Replace href="#enquire" on syllabus button with actual syllabus catalogue URL
    txt = re.sub(
        r'<a class="btn btn-primary" href="#enquire">Get the Complete Course Syllabus</a>',
        f'<a class="btn btn-primary" href="{syl_url}" target="_blank" rel="noopener noreferrer">Get the Complete Course Syllabus &darr;</a>',
        txt
    )
    txt = re.sub(
        r'<a class="btn btn-primary" href="#enquire">Get the Course Syllabus</a>',
        f'<a class="btn btn-primary" href="{syl_url}" target="_blank" rel="noopener noreferrer">Get the Course Syllabus &darr;</a>',
        txt
    )
    txt = re.sub(
        r'<a class="btn btn-primary" href="#enquire">Download Syllabus</a>',
        f'<a class="btn btn-primary" href="{syl_url}" target="_blank" rel="noopener noreferrer">Download Syllabus &darr;</a>',
        txt
    )
    
    # Also in Python course and Machine learning course
    txt = re.sub(
        r'<a class="btn btn-primary" href="#enquiry-form">Get the Complete Course Syllabus</a>',
        f'<a class="btn btn-primary" href="{syl_url}" target="_blank" rel="noopener noreferrer">Get the Complete Course Syllabus &darr;</a>',
        txt
    )
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Linked {page} to {syl_url}!")
