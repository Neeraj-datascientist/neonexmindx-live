import glob

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # If Venkat Nagarjun is mapped to neeraj-neonexmindx
    if '"name": "Venkat Nagarjun"' in txt and '"sameAs": "https://www.linkedin.com/in/neeraj-neonexmindx/"' in txt:
        txt = txt.replace(
            '"name": "Venkat Nagarjun",\n      "jobTitle": "Developer and QA Mentor",\n      "description": "Software developer and QA automation specialist mentoring learners on practical code quality, test frameworks, Python applications, and production readiness.",\n      "worksFor": {\n        "@id": "https://neonexmindx.com/#organization"\n      },\n      "sameAs": "https://www.linkedin.com/in/neeraj-neonexmindx/"',
            '"name": "Venkat Nagarjun",\n      "jobTitle": "Developer and QA Mentor",\n      "description": "Software developer and QA automation specialist mentoring learners on practical code quality, test frameworks, Python applications, and production readiness.",\n      "worksFor": {\n        "@id": "https://neonexmindx.com/#organization"\n      },\n      "sameAs": "https://www.linkedin.com/company/neonex-mindx/"'
        )
        # also handle single line spacing
        txt = txt.replace(
            '"name": "Venkat Nagarjun", "sameAs": "https://www.linkedin.com/in/neeraj-neonexmindx/"',
            '"name": "Venkat Nagarjun", "sameAs": "https://www.linkedin.com/company/neonex-mindx/"'
        )
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        count += 1

print(f"Fixed Venkat schema in {count} files!")

