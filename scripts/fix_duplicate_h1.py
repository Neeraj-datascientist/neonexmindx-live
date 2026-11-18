import re

files = [
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html',
    'deployment_NeoNex/courses/python-programming-course/index.html'
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    c_new = re.sub(
        r'<h1>(Your Dashboard Should Answer a Business Question, Not Just Look Good\.)</h1>',
        r'<div class="hero-title" style="font-size: clamp(2rem, 3.5vw, 2.75rem); font-weight: 800; line-height: 1.18; margin-bottom: 1rem; color: var(--sn-ink, #0B192C);">\1</div>',
        c
    )
    c_new = re.sub(
        r'<h1>(Do Not Just Train a Model\. Learn When to Trust It\.)</h1>',
        r'<div class="hero-title" style="font-size: clamp(2rem, 3.5vw, 2.75rem); font-weight: 800; line-height: 1.18; margin-bottom: 1rem; color: var(--sn-ink, #0B192C);">\1</div>',
        c_new
    )
    c_new = re.sub(
        r'<h1>(Stop Saving Python Tutorials\. Start Writing Python\.)</h1>',
        r'<div class="hero-title" style="font-size: clamp(2rem, 3.5vw, 2.75rem); font-weight: 800; line-height: 1.18; margin-bottom: 1rem; color: var(--sn-ink, #0B192C);">\1</div>',
        c_new
    )
    if c_new != c:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c_new)
        print('Updated:', f)
    else:
        print('No change in:', f)
