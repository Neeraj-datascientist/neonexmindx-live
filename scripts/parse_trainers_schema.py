import json
import re

txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()
scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', txt, re.DOTALL)
for s in scripts:
    try:
        data = json.loads(s)
        # traverse
        def find_persons(obj):
            if isinstance(obj, dict):
                if obj.get('@type') == 'Person':
                    print("  Person:", obj.get('name'), "->", obj.get('sameAs'))
                for v in obj.values():
                    find_persons(v)
            elif isinstance(obj, list):
                for item in obj:
                    find_persons(item)
        find_persons(data)
    except Exception as e:
        print("JSON parse error:", e)
