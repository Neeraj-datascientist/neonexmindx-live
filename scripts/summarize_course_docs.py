import docx

def summarize_doc(path):
    print("="*50)
    print("FILE:", path)
    doc = docx.Document(path)
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t: continue
        if any(t.startswith(prefix) for prefix in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', 'MODULE', 'Stage', 'Topic', 'Chapter']) or len(t) < 40 and not t.startswith('•'):
            print(" -", t[:75])

summarize_doc(r'deployment_NeoNex\syllabus\individual modules\Python (4).docx')
summarize_doc(r'deployment_NeoNex\syllabus\individual modules\SQL  (3).docx')
summarize_doc(r'deployment_NeoNex\syllabus\individual modules\MACHINE LEARNING — COMPLETE ROADMAP (2).docx')

