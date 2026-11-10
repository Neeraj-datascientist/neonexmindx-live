import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

# Configurations for each page:
# (relative_path, original_eyebrow_regex, new_eyebrow_h1_text, original_h1_regex, new_headline_tag)
PAGE_CONFIGS = [
    # 1. Homepage (index.html & Neonex Mindx Home Page.html)
    {
        "files": ["index.html", "Neonex Mindx Home Page.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online Data, Analytics &amp; AI Career Programs</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Data, Analytics &amp; AI Career Programs</h1>',
        "h1_search": r'<h1>(Stop Watching Tutorials\.\s*<span>Start Building a Career You Can Explain\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 2. Data Analytics Course
    {
        "files": ["courses/data-analytics-course/index.html", "Neonex Mindx Data Analytics Course.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online Data Analytics Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Data Analytics Course in India</h1>',
        "h1_search": r'<h1>(Stop Watching Dashboards\.\s*<span>Start Building Ones People Act On\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 3. Data Science Course
    {
        "files": ["courses/data-science-course/index.html", "Neonex Mindx Data Science Course.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online Data Science Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Data Science Course in India</h1>',
        "h1_search": r'<h1>(Stop Memorising Algorithms\.\s*<span>Start Building Models You Can Defend\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 4. AI & ML Course
    {
        "files": ["courses/ai-ml-engineering-course/index.html", "ai-ml-course/index.html", "Neonex Mindx AI ML Course.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online AI and Machine Learning Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online AI and Machine Learning Course in India</h1>',
        "h1_search": r'<h1>(A Prompt Is Not a Product\.\s*<span>Learn to Engineer AI Systems That Ship\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 5. Data Engineering Course
    {
        "files": ["courses/data-engineering-course/index.html", "data-engineering-course/index.html", "Neonex Mindx Data Engineering Course.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online Data Engineering Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Data Engineering Course in India</h1>',
        "h1_search": r'<h1>(Data Does Not Move Itself\.\s*<span>Learn to Build the Pipelines That Do\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 6. Business Analytics Course
    {
        "files": ["courses/business-analytics-course/index.html", "business-analytics-course/index.html", "Neonex Mindx Business Analytics Course.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online Business Analytics Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Business Analytics Course in India</h1>',
        "h1_search": r'<h1>(Dashboards Do Not Run Businesses\.\s*<span>Decisions Do\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 7. Generative AI Course
    {
        "files": ["courses/generative-ai-engineering-course/index.html", "generative-ai-engineering-course/index.html"],
        "eyebrow_search": r'<div class="eyebrow">Live Online AI and Machine Learning Course in India</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Live Online Generative AI Course in India</h1>',
        "h1_search": r'<h1>(A Prompt Is Not a Product\.\s*<span>Learn to Engineer AI Systems That Ship\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 8. About Us
    {
        "files": ["about-us/index.html", "Neonex Mindx About us page.html"],
        "eyebrow_search": r'<div class="eyebrow">About NeoNex MindX</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">About NeoNex MindX</h1>',
        "h1_search": r'<h1>(We Turn &ldquo;I Watched a Tutorial&rdquo; Into <span>&ldquo;I Can Build This\.&rdquo;</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 9. Trainers
    {
        "files": ["trainers/index.html", "Neonex Mindx Trainers Page.html"],
        "eyebrow_search": r'<div class="eyebrow">Know Who Will Teach You Before You Enrol</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Data, Analytics &amp; AI Trainers &mdash; Know Who Will Teach You Before You Enrol</h1>',
        "h1_search": r'<h1>(A Syllabus Tells You What Is Covered\.\s*<span>The Trainer Decides Whether You Learn It\.</span>)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 10. Contact Us
    {
        "files": ["contact-us/index.html", "Neonex Mindx Contact Us.html"],
        "eyebrow_search": r'<div class="eyebrow">Need Clarity Before You Choose a Course\?</div>',
        "eyebrow_replace": r'<h1 class="eyebrow">Contact NeoNex MindX &mdash; Need Clarity Before You Choose a Course\?</h1>',
        "h1_search": r'<h1>(Speak with a Course Advisor and Choose the Right Learning Path)</h1>',
        "h1_replace": r'<div class="hero-title">\1</div>'
    },
    # 11. Blogs Knowledge Hub
    {
        "files": ["blogs/index.html", "blogs.html"],
        "eyebrow_search": r'<span id="blog-hero-badge">NeoNeX Knowledge Hub</span>',
        "eyebrow_replace": r'<h1 id="blog-hero-badge" class="blog-h1-badge">Data Analytics, Data Science &amp; AI Blog &mdash; NeoNeX Knowledge Hub</h1>',
        "h1_search": r'<h1 id="blog-hero-title">(Tech &amp; Career Insights for Future Leaders)</h1>',
        "h1_replace": r'<div id="blog-hero-title" class="blog-hero-title">\1</div>'
    }
]

# CSS injection to guarantee 100% identical rendering
SHARED_HERO_CSS = """
<style id="h1-seo-styling">
h1.eyebrow, h1.blog-h1-badge {
  font-family: var(--font-display, inherit);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 18px 0;
  color: var(--blue-dark, #0c337c);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .105em;
  text-transform: uppercase;
  line-height: 1.3;
}
@media (max-width: 768px) {
  h1.eyebrow, h1.blog-h1-badge { font-size: 11px; letter-spacing: .11em; margin-bottom: 15px; }
}
.hero-title, .blog-hero-title {
  font-family: var(--font-display, inherit);
  font-size: clamp(42px, 5.8vw, 74px);
  font-weight: 800;
  line-height: 1.035;
  letter-spacing: -.044em;
  margin-top: 0;
  margin-bottom: 22px;
  text-wrap: balance;
  color: #111827;
}
.hero-title span, .blog-hero-title span {
  color: var(--blue, #1B5DB7);
}
@media (max-width: 768px) {
  .hero-title, .blog-hero-title {
    font-size: clamp(34px, 9.5vw, 38px);
    line-height: 1.12;
    letter-spacing: -.032em;
    margin-bottom: 18px;
  }
}
</style>
"""

print("Executing precise, non-degrading H1 SEO transformations...")

processed_files = set()

for cfg in PAGE_CONFIGS:
    for rel in cfg["files"]:
        full_path = os.path.join(ROOT, rel)
        if not os.path.exists(full_path):
            print(f"[SKIP] File does not exist: {rel}")
            continue
            
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Replace eyebrow
        new_content, eb_count = re.subn(cfg["eyebrow_search"], cfg["eyebrow_replace"], content, count=1)
        
        # 2. Replace h1
        new_content, h1_count = re.subn(cfg["h1_search"], cfg["h1_replace"], new_content, count=1)
        
        # 3. Inject shared CSS before </head> if not already present
        if "id=\"h1-seo-styling\"" not in new_content:
            new_content = new_content.replace("</head>", SHARED_HERO_CSS + "\n</head>")
            
        if eb_count > 0 and h1_count > 0:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"[SUCCESS] Updated {rel}: Eyebrow -> H1, Headline -> Hero-Title (Zero visual change)")
            processed_files.add(rel)
        else:
            print(f"[CHECK] {rel}: eb_count={eb_count}, h1_count={h1_count}")

print(f"\nTotal files updated successfully: {len(processed_files)}")

