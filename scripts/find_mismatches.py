import os
import re

NIKHIL_LINK = "https://www.linkedin.com/in/nikhil-pc-4a24b619b?utm_source=share_via&utm_content=profile&utm_medium=member_android"
NEERAJ_LINK = "https://www.linkedin.com/in/neeraj-neonexmindx/"

for root, dirs, files in os.walk('deployment_NeoNex'):
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                c = fh.read()
            if 'nikhil' not in c.lower():
                continue
            # Search for chunks or divs where Nikhil appears
            # Let's find all occurrences of 'Nikhil' and inspect 1500 chars before and after
            for m in re.finditer(r'Nikhil', c, re.IGNORECASE):
                start = max(0, m.start() - 600)
                end = min(len(c), m.end() + 600)
                snippet = c[start:end]
                # Check if neeraj linkedin is in this snippet
                if 'neeraj-neonexmindx' in snippet:
                    print(f"=== FOUND MISMATCH in {p} ===")
                    print(snippet)
                    print("="*50)
