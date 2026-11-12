import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
print(f"Total HTML files: {len(files)}")

mismatches = []
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            html = fp.read()
            
        # Match mentor card blocks
        # Let's find mentor names and their corresponding links
        # Common mentors: Neeraj, Nikhil, Yashas, Lakshmi, Raveendran, Nagarjuna
        mentors = ['Nikhil', 'Yashas', 'Lakshmi', 'Raveendran', 'Nagarjuna', 'Neeraj']
        
        # Look for mentor cards or snippets containing mentor name and linkedin
        # e.g., <div class="mentor-card"> ... </div> or similar
        snippets = re.findall(r'(<[^>]+class=["\'][^"\']*(?:mentor|trainer|card)[^"\']*["\'][^>]*>[\s\S]*?</(?:div|article|section)>)', html, re.I)
        for snip in snippets:
            for m in mentors:
                if m in snip:
                    # find all hrefs in snip
                    links = re.findall(r'href=["\']([^"\']+)["\']', snip)
                    for l in links:
                        if 'linkedin.com' in l:
                            mismatches.append((f, m, l))
    except Exception as e:
        pass

print(f"\nTotal Mentor LinkedIn instances found: {len(mismatches)}")
mentor_dict = {}
for f, m, l in mismatches:
    if m not in mentor_dict: mentor_dict[m] = set()
    mentor_dict[m].add(l)

for m, links in mentor_dict.items():
    print(f"\nMentor: {m}")
    for l in links:
        print(f"  - {l}")
