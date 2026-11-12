import glob
import re

files = [
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

floating_btn_html = '''
<!-- Global Floating WhatsApp Button -->
<a href="https://wa.me/918431803839?text=Hi%20NeoNex%20MindX%2C%20I%20am%20interested%20in%20this%20course%20and%20would%20like%20more%20details." 
   class="site-floating-whatsapp" 
   target="_blank" 
   rel="noopener noreferrer" 
   aria-label="Chat on WhatsApp"
   title="Chat with Course Advisor on WhatsApp">
  <svg viewBox="0 0 24 24" width="32" height="32" fill="#ffffff"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.25-.13-1.47-.72-1.7-.81-.23-.08-.39-.13-.56.13-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.13-1.06-.39-2.01-1.24-.74-.66-1.25-1.48-1.39-1.73-.15-.25-.02-.39.11-.51.11-.11.25-.29.37-.43.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.56-1.34-.76-1.84-.2-.49-.4-.42-.56-.43h-.47c-.17 0-.43.06-.66.31-.22.25-.86.84-.86 2.05s.88 2.38 1 2.55c.13.17 1.74 2.66 4.22 3.73.59.25 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.15-1.18-.07-.1-.22-.17-.47-.29z"/></svg>
  <span class="floating-tooltip">Chat with us</span>
</a>

<style>
.site-floating-whatsapp {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: #25D366;
  box-shadow: 0 4px 18px rgba(37, 211, 102, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 99998;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.2s ease;
  text-decoration: none;
}
.site-floating-whatsapp:hover {
  transform: scale(1.08) translateY(-2px);
  box-shadow: 0 6px 24px rgba(37, 211, 102, 0.6);
}
.site-floating-whatsapp .floating-tooltip {
  position: absolute;
  right: 68px;
  background: #0f172a;
  color: #ffffff;
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: 700;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease, transform 0.2s ease;
  transform: translateX(6px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.site-floating-whatsapp:hover .floating-tooltip {
  opacity: 1;
  transform: translateX(0);
}
@media (max-width: 680px) {
  .site-floating-whatsapp {
    bottom: 82px; /* stay above mobile bottom bar */
    right: 16px;
    width: 52px;
    height: 52px;
  }
}
</style>
'''

for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    if 'site-floating-whatsapp' not in txt:
        # inject before </body>
        txt = txt.replace('</body>', floating_btn_html + '\n</body>')
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        print(f"Injected floating WhatsApp button into {f}!")
