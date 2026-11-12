import re

src = 'deployment_NeoNex/courses/data-science-course/index.html'
txt = open(src, 'r', encoding='utf-8').read()

# Let's inspect the tracks
# Track 1: Programming & Analytical Data Foundations (Modules 1-6)
# Track 2: Engineering, Agile & Mathematical Foundations (Modules 7-11)
# Track 3: Machine Learning & AI Foundations (Modules 12-13)
# Track 4: Advanced AI, Deployment & Generative AI (Modules 14-18)

# Find Track 4
track4_match = re.search(r'(<div class="curriculum-track".*?Track 4.*?</div>\s*</div>)', txt, re.DOTALL)
if track4_match:
    print("Found Track 4 in Data Science course! Length:", len(track4_match.group(0)))
else:
    # let's look for Track 4
    idx = txt.find('Track 4')
    if idx != -1:
        print("Found 'Track 4' at:", idx)
        print(txt[idx-50:idx+300])

