import glob
import re

files = glob.glob('deployment_NeoNex/syllabus/catalogues/*.html')

fix_style = '''
<style id="restore-content-style">
/* Ensure all syllabus content is fully expanded and visible */
.topic-content-body {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  padding: 12px 16px !important;
  border-top: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
}
.topic-group {
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
  margin-bottom: 12px !important;
  background: #f8fafc !important;
  display: block !important;
  overflow: hidden !important;
}
.topic-header-toggle {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  padding: 10px 14px !important;
  font-weight: 700 !important;
  font-size: 14.5px !important;
  color: #102a43 !important;
  background: #f1f5f9 !important;
  cursor: pointer !important;
}
.topic-sub-chevron {
  width: 16px !important;
  height: 16px !important;
  transform: rotate(180deg) !important;
  color: #2563eb !important;
}
.bullet-list {
  list-style: none !important;
  padding-left: 0 !important;
  margin: 10px 0 0 0 !important;
}
.bullet-list li {
  position: relative !important;
  padding-left: 22px !important;
  margin-bottom: 8px !important;
  line-height: 1.6 !important;
  color: #334155 !important;
  font-size: 14px !important;
}
.bullet-list li::before {
  content: "✓" !important;
  position: absolute !important;
  left: 4px !important;
  top: 0 !important;
  color: #16a34a !important;
  font-weight: 800 !important;
  font-size: 13px !important;
}
</style>
'''

for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    if 'id="restore-content-style"' not in txt:
        txt = txt.replace('</head>', fix_style + '\n</head>')
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        print(f"Restored content visibility in {f}!")
