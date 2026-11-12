import json

report = json.load(open('deployment_NeoNex/scripts/playwright_report.json', 'r', encoding='utf-8'))

types = {}
for r in report:
    types.setdefault(r['type'], []).append(r)

print(f"Total report items: {len(report)}")
for t, items in types.items():
    print(f"  Type '{t}': {len(items)} items")
    if t == 'HORIZONTAL_OVERFLOW':
        for it in items:
            print("   Overflow in:", it['url'], "at viewport:", it['viewport'], "offending:", it.get('offending'))
    elif t == 'PAGE_LOAD_ERROR':
        for it in items:
            print("   Error in:", it['url'], "error:", it.get('error'))

