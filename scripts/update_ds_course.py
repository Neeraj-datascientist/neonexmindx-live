import re

src = 'deployment_NeoNex/courses/data-science-course/index.html'
content = open(src, 'r', encoding='utf-8').read()

# Replace any link pointing to data-science-and-ai-syllabus with data-science-syllabus
content = content.replace(
    '/syllabus/catalogues/data-science-and-ai-syllabus.html',
    '/syllabus/catalogues/data-science-syllabus.html'
)

# Update Curriculum title and lead if needed
content = content.replace(
    '<h2>Data Science & AI Course Curriculum</h2>',
    '<h2>Data Science Course Curriculum</h2>'
)
content = content.replace(
    'The curriculum begins with programming and data preparation, builds the mathematical foundations required for modelling, progresses through machine learning, deep learning, NLP, computer vision and ends with deployment and generative AI workflows.',
    'The curriculum provides complete mastery over programming, databases, data visualization, business intelligence, data modelling, mathematics & statistics, and machine learning model deployment.'
)

# In the curriculum sections, remove Track 4 (Advanced AI, Deployment & Generative AI modules 14, 15, 16, 18)
# Let's inspect the tracks structure in data-science-course
track_pattern = re.compile(r'(<div class="curriculum-track".*?Track 4.*?</div>\s*</div>)', re.DOTALL)

with open(src, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated data-science-course syllabus references to data-science-syllabus.html!")
