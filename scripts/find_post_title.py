import re

b = 'deployment_NeoNex/blog/2026-breakthroughs-in-ai-agents-llms/index.html'
txt = open(b, 'r', encoding='utf-8').read()
no_script = re.sub(r'<script.*?</script>', '', txt, flags=re.DOTALL)
for m in re.finditer(r'.{0,50}\$\{post\.title\}.{0,50}', no_script):
    print(m.group(0))
