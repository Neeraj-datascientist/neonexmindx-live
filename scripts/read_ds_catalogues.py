import docx

def summarize_docx(path):
    doc = docx.Document(path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    print(f"=== {path} ===")
    print("Paragraphs count:", len(paras))
    for p in paras[:15]:
        print("  ", p)
    print("--- Headings / Key lines ---")
    for p in paras:
        if p.startswith("MODULE") or p.startswith("Module") or "TABLE OF CONTENTS" in p.upper() or p.startswith("PART") or p.startswith("Track"):
            print("  *", p)

summarize_docx('c:/Users/pcnee/Downloads/NEONEX_MINDX_Data_Science_Clickable_Catalogue.docx')
summarize_docx('c:/Users/pcnee/Downloads/NEONEX_MINDX_Data_Science_and_AI_Clickable_Catalogue.docx')
