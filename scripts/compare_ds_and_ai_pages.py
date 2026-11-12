import re

txt_ds = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()
txt_ai = open('deployment_NeoNex/courses/data-science-and-ai-course/index.html', 'r', encoding='utf-8').read()

print("=== DATA SCIENCE COURSE ===")
h1_ds = re.search(r'<h1[^>]*>(.*?)</h1>', txt_ds, re.DOTALL)
print("H1:", h1_ds.group(1).strip() if h1_ds else '')
hero_title_ds = re.search(r'<div class="hero-title"[^>]*>(.*?)</div>', txt_ds, re.DOTALL)
print("Hero Title:", hero_title_ds.group(1).strip() if hero_title_ds else '')

print("\n=== DATA SCIENCE AND AI COURSE ===")
h1_ai = re.search(r'<h1[^>]*>(.*?)</h1>', txt_ai, re.DOTALL)
print("H1:", h1_ai.group(1).strip() if h1_ai else '')
hero_title_ai = re.search(r'<div class="hero-title"[^>]*>(.*?)</div>', txt_ai, re.DOTALL)
print("Hero Title:", hero_title_ai.group(1).strip() if hero_title_ai else '')

