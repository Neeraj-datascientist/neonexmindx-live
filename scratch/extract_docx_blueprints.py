import docx
import os

def docx_to_md(docx_path, md_path):
    doc = docx.Document(docx_path)
    lines = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        style = p.style.name.lower()
        if 'heading 1' in style:
            lines.append(f"\n# {text}\n")
        elif 'heading 2' in style:
            lines.append(f"\n## {text}\n")
        elif 'heading 3' in style:
            lines.append(f"\n### {text}\n")
        elif 'title' in style:
            lines.append(f"\n# {text}\n")
        else:
            lines.append(f"{text}\n")
    
    # Process tables if any
    for t in doc.tables:
        lines.append("\n")
        rows_data = []
        for r in t.rows:
            row_cells = [c.text.strip().replace("\n", " ") for c in r.cells]
            rows_data.append(row_cells)
        if rows_data:
            header = rows_data[0]
            lines.append("| " + " | ".join(header) + " |")
            lines.append("| " + " | ".join(["---"] * len(header)) + " |")
            for row in rows_data[1:]:
                # Ensure correct column count
                padded = row + [""] * (len(header) - len(row))
                lines.append("| " + " | ".join(padded[:len(header)]) + " |")
            lines.append("\n")

    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"Extracted {len(lines)} blocks to {md_path}")

base = "deployment_NeoNex"
edtech_docx = os.path.join(base, "docs", "blueprints", "NeoNex_MindX_EdTech_HLD_LLD_Blueprint.docx")
it_docx = os.path.join(base, "docs", "blueprints", "NeoNex_MindX_IT_Consultancy_HLD_LLD_Blueprint.docx")

docx_to_md(edtech_docx, os.path.join(base, "docs", "blueprints", "NeoNex_MindX_EdTech_HLD_LLD_Blueprint.md"))
docx_to_md(it_docx, os.path.join(base, "docs", "blueprints", "NeoNex_MindX_IT_Consultancy_HLD_LLD_Blueprint.md"))
