import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
forms = []
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    form_matches = re.finditer(r'<form\b([^>]*)>(.*?)</form>', txt, re.DOTALL | re.IGNORECASE)
    for m in form_matches:
        attrs = m.group(1)
        body = m.group(2)
        fid = re.search(r'id=["\']([^"\']*)["\']', attrs)
        action = re.search(r'action=["\']([^"\']*)["\']', attrs)
        btn = re.search(r'<(?:button|input)[^>]*(?:submit|type=["\']submit["\'])[^>]*>', body, re.IGNORECASE)
        forms.append({
            'file': f,
            'id': fid.group(1) if fid else 'NO_ID',
            'action': action.group(1) if action else 'NO_ACTION',
            'has_submit': bool(btn)
        })

print(f"Total forms sitewide: {len(forms)}")
no_submit = [f for f in forms if not f['has_submit']]
print(f"Forms without submit button: {len(no_submit)}")
for ns in no_submit:
    print(" ", ns['file'], ns['id'])

