import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

mentors = [
    ('Nikhil', 'https://www.linkedin.com/in/nikhil-pc-4a24b619b?utm_source=share_via&utm_content=profile&utm_medium=member_android'),
    ('Sanjana', 'https://www.linkedin.com/in/sanjana-j29042000'),
    ('Lakshmi', 'https://www.linkedin.com/in/lakshmi-m-achar-b5a032212/'),
    ('Neeraj', 'https://www.linkedin.com/in/neeraj-neonexmindx/'),
    ('Yashas', 'https://www.linkedin.com/in/yashas-suresh-667475155/'),
    ('Raveendran', 'https://www.linkedin.com/in/raveendran-m-581a723b8/'),
    ('Megha', 'https://www.linkedin.com/in/megha-paul02/'),
    ('Venkat', 'https://www.linkedin.com/company/neonex-mindx/')
]

mismatches = []
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    for name, expected_url in mentors:
        # find cards or sections mentioning the mentor and having a linkedin link
        # e.g., <h3>Nikhil</h3> ... href="..."
        pattern = re.compile(rf'({name}[^<]*</h3>.*?<a\b[^>]*href=[\"\']([^\"\']*)[\"\'][^>]*>)', re.DOTALL | re.IGNORECASE)
        for m in pattern.finditer(txt):
            found_url = m.group(2)
            if 'linkedin.com' in found_url and found_url.rstrip('/') != expected_url.rstrip('/'):
                mismatches.append((f, name, found_url, expected_url))

print(f"Total mentor mismatches: {len(mismatches)}")
for m in mismatches:
    print(" ", m)

