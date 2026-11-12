import docx

def parse_docx(path):
    print("=" * 60)
    print("FILE:", path)
    print("=" * 60)
    doc = docx.Document(path)
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if not t:
            continue
        # Print major headers or structural markers
        if any(keyword in t.upper() for keyword in ["MODULE", "STAGE", "SYLLABUS", "ROADMAP", "OBJECTIVE", "PROJECT", "CAPSTONE"]):
            print(f"P{i}: {t[:100]}")
        elif t.startswith(("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.")):
            if len(t) < 80:
                print(f"  {t}")

for p in [
    r'C:\Users\pcnee\Downloads\COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx',
    r'C:\Users\pcnee\Downloads\NeoNex_MindX_Tableau_Syllabus_Professional.docx',
    r'C:\Users\pcnee\Downloads\Excel,powerbi,generative ai (2).docx'
]:
    parse_docx(p)

