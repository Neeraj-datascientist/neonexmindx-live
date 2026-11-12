import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

forms = []
wa_links = []
li_links = []

for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # Find forms
    f_matches = re.findall(r'<form[^>]*>', txt)
    if f_matches:
        forms.append((f, len(f_matches)))
    # Find wa links
    w_matches = re.findall(r'href=[\"\'][^\"\']*wa\.me[^\"\']*[\"\']', txt)
    if w_matches:
        wa_links.append((f, len(w_matches)))
    # Find linkedin links
    l_matches = re.findall(r'href=[\"\'][^\"\']*linkedin\.com[^\"\']*[\"\']', txt)
    if l_matches:
        li_links.append((f, len(l_matches)))

print(f"Total HTML files with forms: {len(forms)}")
print(f"Total HTML files with WhatsApp links: {len(wa_links)}")
print(f"Total HTML files with LinkedIn links: {len(li_links)}")
