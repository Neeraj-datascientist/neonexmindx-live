import os
import re

print("=== PRECISE CALIBRATION OF SHORT COURSE TRAINER CARDS ===")

short_courses = [
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

nikhil_link = 'https://www.linkedin.com/in/nikhil-pc-4a24b619b?utm_source=share_via&utm_content=profile&utm_medium=member_android'
sanjana_link = 'https://www.linkedin.com/in/sanjana-j29042000'
lakshmi_link = 'https://www.linkedin.com/in/lakshmi-m-achar-b5a032212/'
yashas_link = 'https://www.linkedin.com/in/yashas-suresh-667475155/'
raveendran_link = 'https://www.linkedin.com/in/raveendran-m-581a723b8/'
megha_link = 'https://www.linkedin.com/in/megha-paul02/'
neeraj_link = 'https://www.linkedin.com/in/neeraj-neonexmindx/'

for p in short_courses:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Look for Nikhil trainer card specifically
    # e.g. <article class="trainer-card"><div class="trainer-head"><img data-embed="trainer-nikhil"...><div><h3>Nikhil</h3>...</div></div><a class="linkedin" href="..."
    
    # Simple direct replacement of Nikhil card
    html = re.sub(
        r'(<h3>Nikhil</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{nikhil_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Sanjana</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{sanjana_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Lakshmi</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{lakshmi_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Yashas</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{yashas_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Megha</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{megha_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Neeraj</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{neeraj_link}\2',
        html
    )
    html = re.sub(
        r'(<h3>Raveendran</h3>[\s\S]*?<a class="linkedin" href=")[^"]+(")',
        rf'\1{raveendran_link}\2',
        html
    )

    # Schema Person sameAs
    html = re.sub(r'("name":\s*"Nikhil"[\s\S]*?"sameAs":\s*")[^"]+(")', rf'\1{nikhil_link}\2', html)
    html = re.sub(r'("name":\s*"Sanjana"[\s\S]*?"sameAs":\s*")[^"]+(")', rf'\1{sanjana_link}\2', html)
    html = re.sub(r'("name":\s*"Lakshmi"[\s\S]*?"sameAs":\s*")[^"]+(")', rf'\1{lakshmi_link}\2', html)
    html = re.sub(r'("name":\s*"Yashas"[\s\S]*?"sameAs":\s*")[^"]+(")', rf'\1{yashas_link}\2', html)
    html = re.sub(r'("name":\s*"Megha"[\s\S]*?"sameAs":\s*")[^"]+(")', rf'\1{megha_link}\2', html)

    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Updated {p}")

