import os
import glob
import re

print("=== FIXING ALL TRAINER LINKEDIN PROFILES SITEWIDE ===")

official_links = {
    'nikhil': 'https://www.linkedin.com/in/nikhil-pc-4a24b619b?utm_source=share_via&utm_content=profile&utm_medium=member_android',
    'sanjana': 'https://www.linkedin.com/in/sanjana-j29042000',
    'lakshmi': 'https://www.linkedin.com/in/lakshmi-m-achar-b5a032212/',
    'neeraj': 'https://www.linkedin.com/in/neeraj-neonexmindx/',
    'yashas': 'https://www.linkedin.com/in/yashas-suresh-667475155/',
    'raveendran': 'https://www.linkedin.com/in/raveendran-m-581a723b8/',
    'megha': 'https://www.linkedin.com/in/megha-paul02/'
}

root = 'deployment_NeoNex'
html_files = glob.glob(f'{root}/**/*.html', recursive=True)

fixed_instances = 0
fixed_files = 0

for fp in html_files:
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        
        # 1. Look for trainer cards: <article class="trainer-card"> or <article class="mentor-card">
        # In python course and others:
        # e.g.:
        # <article class="trainer-card"><div class="trainer-head"><img data-embed="trainer-nikhil"...><div><h3>Nikhil</h3>...</div></div><a class="linkedin" href="https://www.linkedin.com/"...
        
        for name, link in official_links.items():
            # Pattern A: trainer-card with trainer-name
            # Replace generic linkedin href in card containing name
            pattern = rf'(<article[^>]*class=["\'](?:trainer-card|mentor-card)["\'][^>]*>[\s\S]*?<h3>\s*{name}\b[\s\S]*?<a[^>]*href=["\'])([^"\']+)(["\'][^>]*>)'
            
            def replace_card_link(match):
                prefix, old_url, suffix = match.group(1), match.group(2), match.group(3)
                if old_url != link:
                    return f"{prefix}{link}{suffix}"
                return match.group(0)

            new_content = re.sub(pattern, replace_card_link, new_content, flags=re.I)
            
            # Pattern B: Reverse order in card (where <a> precedes <h3> or contains <h3>)
            pattern_rev = rf'(<a[^>]*href=["\'])([^"\']+)(["\'][^>]*>[\s\S]*?<h3>\s*{name}\b[\s\S]*?</article>)'
            def replace_card_link_rev(match):
                prefix, old_url, suffix = match.group(1), match.group(2), match.group(3)
                if 'linkedin.com' in old_url and old_url != link:
                    return f"{prefix}{link}{suffix}"
                return match.group(0)
            new_content = re.sub(pattern_rev, replace_card_link_rev, new_content, flags=re.I)

            # Pattern C: JSON-LD Schema Person sameAs
            pattern_schema = rf'("@type":\s*"Person"[\s\S]*?"name":\s*"{name}"[\s\S]*?"sameAs":\s*")[^"]+(")'
            def replace_schema(match):
                return f"{match.group(1)}{link}{match.group(2)}"
            new_content = re.sub(pattern_schema, replace_schema, new_content, flags=re.I)

        if new_content != content:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files += 1

    except Exception as e:
        print(f"Error processing {fp}: {e}")

print(f"Successfully calibrated mentor LinkedIn links across {fixed_files} files sitewide.")

