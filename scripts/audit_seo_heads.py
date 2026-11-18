import glob, os

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

issues = []

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        c = fh.read()
    
    # 1. Check title
    if '<title>' not in c.lower():
        issues.append((f, 'MISSING_TITLE'))
    # 2. Check meta viewport
    if 'viewport' not in c.lower():
        issues.append((f, 'MISSING_VIEWPORT'))
    # 3. Check meta description
    if 'name="description"' not in c.lower() and "name='description'" not in c.lower() and 'id="meta-desc"' not in c.lower():
        if 'syllabus/catalogues' not in f.replace('\\', '/') and 'cms' not in f.replace('\\', '/') and 'crm' not in f.replace('\\', '/'):
            issues.append((f, 'MISSING_META_DESC'))
    # 4. Check canonical
    if 'rel="canonical"' not in c.lower() and "rel='canonical'" not in c.lower() and 'id="canonical-link"' not in c.lower():
        if 'syllabus/catalogues' not in f.replace('\\', '/') and 'cms' not in f.replace('\\', '/') and 'crm' not in f.replace('\\', '/'):
            issues.append((f, 'MISSING_CANONICAL'))

print(f'Total SEO head tag issues: {len(issues)}')
for iss in issues[:30]:
    print(iss[0], '-->', iss[1])
