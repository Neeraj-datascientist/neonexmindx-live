import docx

def summarize_docx(path):
    doc = docx.Document(path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    print(f"=== {path} ===")
    print("Paragraphs count:", len(paras))
    for p in paras[:10]:
        print("  ", p)
    print("--- Headings / Key lines ---")
    for p in paras:
        if p.startswith("MODULE") or p.startswith("Module") or "TABLE OF CONTENTS" in p.upper() or p.startswith("PART") or p.startswith("Track"):
            print("  *", p)

try:
    summarize_docx('c:/Users/pcnee/Downloads/Data science and AI.docx')
except Exception as e:
    print("Error:", e)

try:
    summarize_docx('c:/Users/pcnee/Downloads/Certified Data Science Professional.docx')
except Exception as e:
    print("Error:", e)

