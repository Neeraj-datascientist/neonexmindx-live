import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

# Look for hero metadata or quick overview or course details
hero = re.search(r'<section class="hero[^"]*".*?</section>', txt, re.DOTALL)
if hero:
    print("=== HERO IN DATA SCIENCE COURSE ===")
    print(hero.group(0)[:1200])

# Look for duration text
for m in re.finditer(r'(duration|months|weeks|hours)', txt, re.IGNORECASE):
    snippet = txt[max(0, m.start()-40):min(len(txt), m.end()+60)]
    print("Match:", snippet.replace('\n', ' '))
    if 'month' in snippet.lower():
        print("  -> FOUND MONTH!")
