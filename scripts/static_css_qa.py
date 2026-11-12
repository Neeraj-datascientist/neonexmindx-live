import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

issues = []

for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    
    # 1. Check for fixed pixel widths > 360px on containers or layout elements
    fixed_widths = re.findall(r'style=[\"\'][^\"\']*width:\s*([4-9]\d{2,}|\d{4,})px[^\"\']*[\"\']', txt)
    if fixed_widths:
        issues.append((f, "FIXED_PIXEL_WIDTH", fixed_widths))
        
    # 2. Check for missing viewport meta tag
    if '<meta name="viewport"' not in txt and '<meta content="width=device-width' not in txt:
        issues.append((f, "MISSING_VIEWPORT", None))
        
    # 3. Check for SVG viewBox or width/height issues
    svgs_without_viewbox = re.findall(r'<svg(?![^>]*viewBox)[^>]*>', txt)
    if svgs_without_viewbox:
        # ignore if width and height are explicitly defined or if defs
        bad_svgs = [s for s in svgs_without_viewbox if 'width=' not in s or 'height=' not in s]
        if bad_svgs:
            issues.append((f, "SVG_NO_VIEWBOX_OR_DIMENSIONS", len(bad_svgs)))

print(f"Total HTML files scanned: {len(files)}")
print(f"Static issues found: {len(issues)}")
for iss in issues[:15]:
    print(" ", iss)

