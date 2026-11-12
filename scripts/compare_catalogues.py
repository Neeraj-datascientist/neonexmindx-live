import re

ds_cat = open('deployment_NeoNex/syllabus/catalogues/data-science-syllabus.html', 'r', encoding='utf-8').read()
ds_ai_cat = open('deployment_NeoNex/syllabus/catalogues/data-science-and-ai-syllabus.html', 'r', encoding='utf-8').read()

def get_modules(html):
    # look for headers or module titles
    titles = re.findall(r'<h[234][^>]*>(.*?)</h[234]>', html)
    return [t.strip() for t in titles if 'module' in t.lower() or 'part' in t.lower() or 'track' in t.lower() or len(t.strip()) < 60]

print("=== DATA SCIENCE CATALOGUE ===")
print("Title:", re.search(r'<title>(.*?)</title>', ds_cat).group(1))
for m in get_modules(ds_cat)[:15]:
    print(" ", m)

print("\n=== DATA SCIENCE AND AI CATALOGUE ===")
print("Title:", re.search(r'<title>(.*?)</title>', ds_ai_cat).group(1))
for m in get_modules(ds_ai_cat)[:15]:
    print(" ", m)

