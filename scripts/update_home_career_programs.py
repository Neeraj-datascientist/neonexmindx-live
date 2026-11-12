import re

txt = open('deployment_NeoNex/index.html', 'r', encoding='utf-8').read()

# 1. Update Eyebrow and heading if needed
txt = txt.replace(
    '<div class="eyebrow">Five Career Programs</div>',
    '<div class="eyebrow">Six Career Programs</div>'
)
txt = txt.replace(
    '<h2>Compare the Five Career Programs</h2>',
    '<h2>Compare the Six Career Programs</h2>'
)
txt = txt.replace(
    'Choose from five career programs and four focused courses',
    'Choose from six career programs and four focused courses'
)

# 2. Update filters to include data-science-ai or keep filters clean
# Current filters:
# <button class="filter active" data-filter="all" type="button">All Programs</button>
# <button class="filter" data-filter="analytics" type="button">Dashboards &amp; Insights</button>
# <button class="filter" data-filter="science" type="button">Predictive Models</button>
# <button class="filter" data-filter="ai" type="button">AI Applications</button>
# <button class="filter" data-filter="engineering" type="button">Data Pipelines</button>
# <button class="filter" data-filter="business" type="button">KPI &amp; Strategy</button>

# 3. Add Data Science and AI card right after Data Science card
ds_card = '''            <article class="program-card" data-category="science">
              <div class="program-head">
                <span class="program-icon"
                  ><svg class="icon"><use href="#i-model"></use></svg></span
                ><span class="duration">9&ndash;11 Months</span>
              </div>
              <h3>Professional Program in Data Science</h3>
              <p>Explore data, build predictive models, evaluate results and present end-to-end solutions.</p>
              <div class="meta-block">
                <b>Best suited for</b
                ><span
                  >Graduates, analysts, IT professionals and career switchers seeking deeper programming and modelling
                  skills.</span
                >
              </div>
              <div class="chips">
                <span class="chip">Python</span><span class="chip">SQL</span><span class="chip">Statistics</span
                ><span class="chip">Machine Learning</span><span class="chip">Deployment</span>
              </div>
              <div class="meta-block">
                <b>Career paths</b
                ><span
                  >Junior Data Scientist, ML Analyst, Data Science Associate and Predictive Analytics Analyst.</span
                >
              </div>
              <a class="program-cta" href="/courses/data-science-course/">Explore Data Science &rarr;</a>
            </article>'''

ds_ai_card = '''            <article class="program-card" data-category="science">
              <div class="program-head">
                <span class="program-icon"
                  ><svg class="icon"><use href="#i-ai"></use></svg></span
                ><span class="duration">10&ndash;11 Months</span>
              </div>
              <h3>Master Program in Data Science &amp; AI</h3>
              <p>Master end-to-end Data Science, Deep Learning, NLP, Computer Vision, MLOps, and Generative AI application engineering.</p>
              <div class="meta-block">
                <b>Best suited for</b
                ><span
                  >Graduates, developers, and engineers wanting full-stack mastery across both classical Data Science and advanced modern AI architectures.</span
                >
              </div>
              <div class="chips">
                <span class="chip">Python &amp; SQL</span><span class="chip">Machine Learning</span><span class="chip">Deep Learning</span
                ><span class="chip">NLP &amp; CV</span><span class="chip">Generative AI</span>
              </div>
              <div class="meta-block">
                <b>Career paths</b
                ><span
                  >Data Scientist, AI Engineer, Machine Learning Engineer, NLP Specialist and Enterprise AI Architect.</span
                >
              </div>
              <a class="program-cta" href="/courses/data-science-and-ai-course/">Explore Data Science &amp; AI &rarr;</a>
            </article>'''

# Replace old DS card with updated DS card + DS AI card
old_ds_card = '''            <article class="program-card" data-category="science">
              <div class="program-head">
                <span class="program-icon"
                  ><svg class="icon"><use href="#i-model"></use></svg></span
                ><span class="duration">6&ndash;7 Months</span>
              </div>
              <h3>Professional Program in Data Science</h3>
              <p>Explore data, build predictive models, evaluate results and present end-to-end solutions.</p>
              <div class="meta-block">
                <b>Best suited for</b
                ><span
                  >Graduates, analysts, IT professionals and career switchers seeking deeper programming and modelling
                  skills.</span
                >
              </div>
              <div class="chips">
                <span class="chip">Python</span><span class="chip">SQL</span><span class="chip">Statistics</span
                ><span class="chip">Machine Learning</span><span class="chip">Deployment</span>
              </div>
              <div class="meta-block">
                <b>Career paths</b
                ><span
                  >Junior Data Scientist, ML Analyst, Data Science Associate and Predictive Analytics Analyst.</span
                >
              </div>
              <a class="program-cta" href="/courses/data-science-course/">Explore Data Science &rarr;</a>
            </article>'''

if old_ds_card in txt:
    txt = txt.replace(old_ds_card, ds_card + '\n' + ds_ai_card)
    print("Successfully added Data Science & AI card to Home programGrid!")
else:
    print("Could not find exact old_ds_card match!")

# 4. Update compare table to include Data Science & AI row
old_compare_row = '''                <tr>
                  <td>Data Science</td>
                  <td>Explore data and build predictive models</td>
                  <td>Python, SQL, statistics, machine learning</td>
                  <td>Analytical learners seeking deeper modelling skills</td>
                </tr>'''

new_compare_rows = '''                <tr>
                  <td>Data Science</td>
                  <td>Explore data, statistical inference and build predictive models</td>
                  <td>Python, SQL, statistics, machine learning, deployment</td>
                  <td>Analytical learners seeking deeper modelling skills</td>
                </tr>
                <tr>
                  <td>Data Science &amp; AI</td>
                  <td>Complete Data Science core plus Deep Learning, NLP, Computer Vision &amp; Generative AI</td>
                  <td>Python, SQL, ML, Deep Learning, NLP, CV, LLMs, RAG</td>
                  <td>Learners and developers wanting complete Data Science &amp; AI dual-mastery</td>
                </tr>'''

if old_compare_row in txt:
    txt = txt.replace(old_compare_row, new_compare_rows)
    print("Successfully added Data Science & AI row to comparison table!")
else:
    print("Could not find exact old_compare_row match!")

with open('deployment_NeoNex/index.html', 'w', encoding='utf-8') as f:
    f.write(txt)

