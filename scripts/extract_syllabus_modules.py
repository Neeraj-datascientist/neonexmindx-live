import docx
import os

docs = [
    r"C:\Users\pcnee\Downloads\NeoNex_MindX_Tableau_Syllabus_Professional.docx",
    r"C:\Users\pcnee\Downloads\COMBO_COURSE_Excel_PowerBI_GenerativeAI_final (1).docx"
]

for d in docs:
    print("=" * 60)
    print(os.path.basename(d))
    print("=" * 60)
    doc = docx.Document(d)
    modules = []
    for p in doc.paragraphs:
        t = p.text.strip()
        if any(t.upper().startswith(k) for k in ["MODULE", "STAGE", "PART", "SECTION", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8."]) and len(t) < 100:
            modules.append(t)
    print(f"Total potential module/topic headers found: {len(modules)}")
    for m in modules[:25]:
        print("  *", m)

