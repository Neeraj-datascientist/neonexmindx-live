import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

# Look for course grid or section with courses we offer
matches = re.findall(r'<section[^>]*courses[^>]*>.*?</section>', txt, re.DOTALL | re.IGNORECASE)
print(f"Sections matching 'courses': {len(matches)}")

# Look for 'courses we offer' or similar heading
for m in re.finditer(r'(courses|programs|curriculum)', txt, re.IGNORECASE):
    snippet = txt[max(0, m.start()-100):min(len(txt), m.end()+300)]
    if '<h2>' in snippet or '<h3>' in snippet or 'class="card' in snippet or 'program-card' in snippet:
        print("--- Match ---")
        print(snippet[:300])
        print("...")
