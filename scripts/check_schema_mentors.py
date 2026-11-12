import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

schema_trainers = []
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # find all Person schemas
    persons = re.findall(r'\{\s*"@type":\s*"Person"[^}]*\}', txt, re.DOTALL)
    for p in persons:
        name = re.search(r'"name":\s*"([^"]*)"', p)
        sameas = re.search(r'"sameAs":\s*"([^"]*)"', p)
        if name and sameas:
            schema_trainers.append((name.group(1), sameas.group(1)))

print(f"Total Person schemas found: {len(schema_trainers)}")
unique_pairs = set(schema_trainers)
for name, sameas in sorted(unique_pairs):
    print(f"  {name} -> {sameas}")
