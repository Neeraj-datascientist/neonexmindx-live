import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
print(f"Total HTML files: {len(files)}")

excel_nav_links = {}
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            # find all <a> tags mentioning Excel
            tags = re.findall(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]*Excel[^<]*)</a>', content, re.I)
            for href, text in tags:
                if href not in excel_nav_links:
                    excel_nav_links[href] = []
                excel_nav_links[href].append(f)
    except Exception as e:
        pass

for href, flist in excel_nav_links.items():
    print(f"\nHREF: '{href}' (Found in {len(flist)} files, e.g. {flist[0]})")

