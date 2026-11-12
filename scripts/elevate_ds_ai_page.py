import re

path = 'deployment_NeoNex/courses/data-science-and-ai-course/index.html'
txt = open(path, 'r', encoding='utf-8').read()

# 1. Update Title and meta description
txt = txt.replace(
    '<title>Data Science and AI Course Online India | NeoNex MindX</title>',
    '<title>Data Science & Artificial Intelligence Master Course | NeoNex MindX</title>'
)

# 2. Update Hero eyebrow and title
txt = txt.replace(
    '<h1 class="eyebrow">Live Online Data Science and AI Master Course in India</h1>',
    '<h1 class="eyebrow">Flagship Master Program &bull; Dual Track Specialization</h1>'
)

txt = txt.replace(
    '<div class="hero-title">Stop Memorising Algorithms. <span>Start Building Models You Can Defend.</span></div>',
    '<div class="hero-title">Master Data Science First. <span>Architect Enterprise AI Systems Next.</span></div>'
)

# 3. Update Hero Lead
old_lead = '''<p class="lead">
              Knowing Python syntax is not enough to become confident in data science. You need to understand the data,
              select the right method, evaluate the model, explain its limits and turn the result into something another
              person can use.
            </p>'''

new_lead = '''<p class="lead">
              The complete master program uniting classical data science with state-of-the-art AI engineering: from Python, SQL, MongoDB and predictive machine learning models to deep neural networks, Transformers, NLP, Computer Vision, MLOps, and production Generative AI applications.
            </p>'''

txt = txt.replace(old_lead, new_lead)

# 4. Update Hero Points
old_points = '''            <ul class="hero-points">
              <li><span class="check" aria-hidden="true">&#10003;</span><span>Structured 10&ndash;11 month learning path</span></li>
              <li>
                <span class="check" aria-hidden="true">&#10003;</span><span>Live online sessions with mentor support</span>
              </li>
              <li>
                <span class="check" aria-hidden="true">&#10003;</span><span>Python, SQL, statistics and machine learning</span>
              </li>
              <li>
                <span class="check" aria-hidden="true">&#10003;</span><span>Model deployment and portfolio projects</span>
              </li>
            </ul>'''

new_points = '''            <ul class="hero-points">
              <li><span class="check" aria-hidden="true">&#10003;</span><span>Complete 10&ndash;11 Month Dual-Track Master Program</span></li>
              <li><span class="check" aria-hidden="true">&#10003;</span><span>18 Comprehensive Modules: DS Core &rarr; AI Foundations &rarr; Deep Learning &rarr; Generative AI</span></li>
              <li><span class="check" aria-hidden="true">&#10003;</span><span>Hands-on Deep Learning, NLP (Transformers/BERT), Computer Vision &amp; MLOps Deployment</span></li>
              <li><span class="check" aria-hidden="true">&#10003;</span><span>Full Generative AI Crash Course: LLMs, LangChain, Vector Databases, RAG &amp; AI Agents</span></li>
            </ul>'''

txt = txt.replace(old_points, new_points)

# 5. Update Curriculum Overview Header
txt = txt.replace(
    '<h2>Data Science & AI Course Curriculum</h2>',
    '<h2>Complete 18-Module Data Science &amp; Artificial Intelligence Curriculum</h2>'
)

# 6. Ensure hero syllabus button points directly to the syllabus catalogue
txt = re.sub(
    r'<a class="btn btn-primary" href="#overview-form">Get the Complete Course Syllabus</a>',
    '<a class="btn btn-primary" href="/syllabus/catalogues/data-science-and-ai-syllabus.html" target="_blank" rel="noopener noreferrer">Get the Complete Master Syllabus &darr;</a>',
    txt
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("Professionally elevated courses/data-science-and-ai-course/index.html!")

