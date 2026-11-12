import glob
import re
import os
import shutil

print("=== FIXING LINKEDIN SVG ICON ACROSS ALL BLOG POSTS ===")

root = 'deployment_NeoNex'
files = glob.glob(f'{root}/blog/*/index.html') + [f'{root}/blog-post.html']

linkedin_svg = '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.64a1.64 1.64 0 1 0 1.64 1.64 1.64 1.64 0 0 0-1.64-1.64Z"/></svg>'
copy_link_svg = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>'

fixed_count = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    new_html = html
    # In share-in:
    # replace <a ... class="share-btn share-in">\s*<span>LinkedIn</span>
    pattern_in = r'(<a[^>]*class=["\']share-btn share-in["\'][^>]*>)\s*(?:<svg[^>]*>.*?</svg>\s*)?<span>LinkedIn</span>'
    replacement_in = rf'\1\n                {linkedin_svg}\n                <span>LinkedIn</span>'
    new_html = re.sub(pattern_in, replacement_in, new_html, flags=re.DOTALL)

    # In copy link button:
    pattern_copy = r'(<button class=["\']share-btn["\'][^>]*onclick=["\'][^"\']*["\'][^>]*>)\s*(?:<svg[^>]*>.*?</svg>\s*)?<span>Copy Link</span>'
    replacement_copy = rf'\1\n                {copy_link_svg}\n                <span>Copy Link</span>'
    new_html = re.sub(pattern_copy, replacement_copy, new_html, flags=re.DOTALL)

    if new_html != html:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_html)
        fixed_count += 1
        print(f"Fixed icons in {fp}")

print(f"Completed! Fixed LinkedIn and Copy Link SVG icons in {fixed_count} blog files.")
