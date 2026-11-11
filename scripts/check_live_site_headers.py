import urllib.request
import re

req = urllib.request.Request('https://neonexmindx.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

can = re.findall(r'<link[^>]+canonical[^>]*>', html, re.I)
desc = re.findall(r'<meta[^>]+name=["\']description["\'][^>]*>', html, re.I)
fb_pixel = re.findall(r'<noscript><img[^>]*>', html, re.I)

print(f"Live site status:")
print(f"  Canonical count: {len(can)}")
for c in can:
    print(f"    {c}")
print(f"  Description count: {len(desc)}")
for d in desc:
    print(f"    {d}")
print(f"  Facebook noscript images: {fb_pixel}")

