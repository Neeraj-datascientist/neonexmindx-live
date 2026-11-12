import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\crm\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

print(f"File size: {len(txt)} bytes")
title = re.search(r'<title>(.*?)</title>', txt, re.I)
print(f"Title: {title.group(1) if title else 'NONE'}")

integrations = re.findall(r'Integrations Hub & Lead Connectors|Google|Meta|Facebook|Webhook', txt, re.I)
print(f"Integration keywords count: {len(integrations)}")

# Find sections
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', txt, re.I)
print(f"Sections in CRM: {sections}")

# Look for lead forms or endpoints
forms = re.findall(r'<form[^>]*>', txt, re.I)
print(f"Forms in CRM: {len(forms)}")

