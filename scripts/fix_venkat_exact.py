import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    
    # We want to replace "sameAs": "https://www.linkedin.com/in/neeraj-neonexmindx/" where name is Venkat Nagarjun
    pattern = re.compile(r'("name":\s*"Venkat Nagarjun".*?"sameAs":\s*")https://www\.linkedin\.com/in/neeraj-neonexmindx/(")', re.DOTALL)
    if pattern.search(txt):
        txt = pattern.sub(r'\1https://www.linkedin.com/company/neonex-mindx/\2', txt)
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        count += 1

print(f"Corrected Venkat sameAs in {count} files!")
