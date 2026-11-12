import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

m = re.search(r'<header.*?</header>', txt, re.DOTALL)
if m:
    print("=== HEADER IN SQL COURSE ===")
    print(m.group(0))

m_mob = re.search(r'<div class="mobile-actions".*?</div>', txt, re.DOTALL)
if m_mob:
    print("=== MOBILE ACTIONS IN SQL COURSE ===")
    print(m_mob.group(0))
