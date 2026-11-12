import glob
import re

files = glob.glob('deployment_NeoNex/blog/*/index.html') + ['deployment_NeoNex/blog-post.html']

old_css = '''@media (max-width: 1024px) {
      .article-grid {
        display: flex !important;
        flex-direction: column !important;
      }
      .article-sidebar {
        display: contents !important;
      }
      #toc-widget {
        order: -1 !important;
        margin-bottom: 24px !important;
        position: static !important;
        width: 100% !important;
      }
      .article-body {
        order: 1 !important;
        width: 100% !important;
      }
      .enquire-sidebar-widget {
        order: 2 !important;
        margin-top: 24px !important;
        width: 100% !important;
      }
    }'''

new_css = '''@media (max-width: 1024px) {
      .article-grid {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .article-sidebar {
        display: contents !important;
      }
      #toc-widget {
        order: -1 !important;
        margin-bottom: 24px !important;
        position: static !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
      .article-body {
        order: 1 !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        overflow-wrap: break-word !important;
        word-break: break-word !important;
      }
      .enquire-sidebar-widget {
        order: 2 !important;
        margin-top: 24px !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
    }'''

count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    if old_css in txt:
        txt = txt.replace(old_css, new_css)
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        count += 1

print(f"Updated responsive blog styles in {count} files!")

