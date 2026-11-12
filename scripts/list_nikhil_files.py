import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    if 'nikhil' in c.lower():
        links = re.findall(r'href=[\'"](https://[^\'"]*linkedin[^\'"]*)[\'"]', c, re.IGNORECASE)
        print(f'{f}: {len(links)} linkedin links')
        for l in sorted(list(set(links))):
            print(f'   {l}')

