import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

# Let's inspect the top 200 lines or search for course names at the top
lines = txt.splitlines()
print("Top 150 lines:")
for i, l in enumerate(lines[:150]):
    if 'course' in l.lower() or 'program' in l.lower() or 'offer' in l.lower() or 'hero' in l.lower():
        print(f"{i+1}: {l}")
