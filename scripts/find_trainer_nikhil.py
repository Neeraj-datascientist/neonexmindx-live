import os
import re

for root, dirs, files in os.walk('deployment_NeoNex'):
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        if f.endswith(('.html', '.js')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                c = fh.read()
            if 'trainer-nikhil' in c.lower():
                print(f"File with trainer-nikhil: {p}")
                # check what linkedin link appears near trainer-nikhil
                for m in re.finditer(r'trainer-nikhil', c, re.IGNORECASE):
                    start = max(0, m.start() - 400)
                    end = min(len(c), m.end() + 800)
                    print(c[start:end])
                    print("-" * 40)
