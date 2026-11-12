import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

# 1. Fix old phone number 8088104708 to official 8431803839
wa_count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    if '8088104708' in txt:
        txt = txt.replace('918088104708', '918431803839')
        txt = txt.replace('8088104708', '8431803839')
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        wa_count += 1

print(f"Updated old WhatsApp phone number in {wa_count} files!")

# 2. Fix Venkat generic linkedin in course pages
li_count = 0
venkat_li = 'https://www.linkedin.com/company/neonex-mindx/'
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # Check if Venkat has href="https://www.linkedin.com/"
    if 'href="https://www.linkedin.com/"' in txt:
        txt = txt.replace('href="https://www.linkedin.com/"', f'href="{venkat_li}"')
        txt = txt.replace('"sameAs": "https://www.linkedin.com/"', f'"sameAs": "{venkat_li}"')
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        li_count += 1

print(f"Updated generic LinkedIn in {li_count} files!")
