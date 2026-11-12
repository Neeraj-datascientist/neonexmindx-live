import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

invalid_wa = []
invalid_li = []

for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    
    # check wa links
    wa = re.findall(r'href=[\"\']([^\"\']*wa\.me[^\"\']*)[\"\']', txt)
    for w in wa:
        if 'wa.me/918431803839' not in w and 'wa.me/?text=' not in w:
            invalid_wa.append((f, w))
            
    # check linkedin links
    li = re.findall(r'href=[\"\']([^\"\']*linkedin\.com[^\"\']*)[\"\']', txt)
    for l in li:
        if 'linkedin.com/company/neonex-mindx/' not in l and \
           'linkedin.com/sharing/share-offsite/' not in l and \
           'linkedin.com/in/' not in l:
            invalid_li.append((f, l))

print("Invalid WA links:", len(invalid_wa), invalid_wa[:5])
print("Invalid LinkedIn links:", len(invalid_li), invalid_li[:5])

