import glob
import re

files = glob.glob('deployment_NeoNex/syllabus/catalogues/*.html')

clean_css = '''
<style>
/* Clean up empty topic groups and restore rich visual styling */
.topic-group:empty {
  display: none !important;
}
.topic-content-body:empty {
  display: none !important;
}
/* Ensure bullet list and topics are clean and visible */
.bullet-list {
  list-style: none !important;
  padding-left: 0 !important;
  margin: 8px 0 0 0 !important;
}
.bullet-list li {
  position: relative !important;
  padding-left: 20px !important;
  margin-bottom: 8px !important;
  line-height: 1.55 !important;
  color: #334155 !important;
}
.bullet-list li::before {
  content: "•";
  position: absolute;
  left: 6px;
  top: 0;
  color: #2563eb;
  font-weight: bold;
}
.topic-group {
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  margin-bottom: 12px !important;
  background: #f8fafc !important;
  padding: 12px 16px !important;
}
.topic-title {
  font-weight: 700 !important;
  font-size: 14.5px !important;
  color: #0f172a !important;
}
</style>
'''

cleaned_count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    
    # Remove empty topic groups completely via regex
    # Match <div class="topic-group[^"]*">\s*</div>
    txt_new = re.sub(r'<div class="topic-group[^"]*">\s*</div>', '', txt)
    
    # Also inject clean CSS
    if 'Clean up empty topic groups' not in txt_new:
        txt_new = txt_new.replace('</head>', clean_css + '\n</head>')
        
    if txt_new != txt:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt_new)
        cleaned_count += 1
        print(f"Cleaned empty topic groups in {f}!")

print(f"Done! Cleaned {cleaned_count} catalogue files.")

