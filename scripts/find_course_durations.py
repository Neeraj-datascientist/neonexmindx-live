import glob
import re

files = glob.glob('deployment_NeoNex/courses/**/index.html', recursive=True)
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.DOTALL)
    # search for duration
    durations = re.findall(r'(\d+[\s–\-\w]*\s*(?:months?|weeks?|hours?))', txt, re.IGNORECASE)
    print(f"\n{f}:")
    print("  H1:", h1.group(1).strip() if h1 else 'None')
    # look for hero meta or stats
    stats = re.findall(r'<div class="hero-stat"[^>]*>.*?</div>', txt, re.DOTALL)
    if stats:
        for s in stats:
            print("  Stat:", ' '.join(re.sub(r'<[^>]+>', ' ', s).split()))
    else:
        # find any duration badge
        d_badge = re.findall(r'class="[^"]*duration[^"]*"[^>]*>(.*?)<', txt)
        print("  Duration badges:", d_badge[:3])

