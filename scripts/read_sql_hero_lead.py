import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

m = re.search(r'<div class="hero-actions".*?</div>', txt, re.DOTALL)
if m:
    print("=== HERO ACTIONS ===")
    print(m.group(0))

m_form = re.search(r'<div class="lead-panel".*?</div>\s*</div>', txt, re.DOTALL)
if m_form:
    print("=== LEAD PANEL / FORM ===")
    print(m_form.group(0)[:800])
