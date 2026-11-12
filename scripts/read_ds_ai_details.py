import docx

doc = docx.Document('c:/Users/pcnee/Downloads/NEONEX_MINDX_Data_Science_and_AI_Clickable_Catalogue.docx')
paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

print("Total non-empty paragraphs:", len(paras))
for p in paras[:30]:
    print("  ", p)

print("\n--- Looking for duration & summary info ---")
for p in paras:
    if any(k in p.lower() for k in ['duration:', 'months', 'weeks', 'part i', 'part ii', 'part iii', 'part iv', 'part v', 'overview']):
        if len(p) < 120:
            print("  *", p)

