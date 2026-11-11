import urllib.request
import json
import xml.etree.ElementTree as ET
import os

HOST = "neonexmindx.com"
KEY = "3d806e385e264c3194ec3c35c892cb9e"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# 1. Load URLs from sitemap
sitemap_path = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    root = ET.fromstring(f.read())
urls = [loc.text for loc in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": urls
}

print(f"Submitting {len(urls)} URLs to IndexNow endpoints...")

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

req_data = json.dumps(payload).encode("utf-8")

for ep in endpoints:
    req = urllib.request.Request(
        ep,
        data=req_data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "NeoNeX-MindX-IndexNow/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"[{ep}] Response HTTP {resp.status} - IndexNow batch accepted successfully!")
    except urllib.error.HTTPError as e:
        # HTTP 200: OK, HTTP 202: Accepted
        print(f"[{ep}] Response HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"[{ep}] Error: {e}")
