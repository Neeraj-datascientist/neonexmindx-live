import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

# Pattern to find each <details class="module" ...> ... </details>
details_blocks = re.findall(r'<details class="module"[^>]*>.*?</details>', txt, re.DOTALL)
print(f"Total details.module blocks: {len(details_blocks)}")

# In Data Science Core:
# We keep Modules 1 to 13 (Python to AI Foundation) and Module 17 (Model Deployment).
# We remove Modules 14 (Deep Learning), 15 (NLP), 16 (Computer Vision), and 18 (Generative AI Practical Crash Course)
# which are exclusive to the Data Science & AI Master Course!

to_remove = []
for b in details_blocks:
    if any(m in b for m in ['DEEP LEARNING', 'NATURAL LANGUAGE PROCESSING', 'COMPUTER VISION', 'GENERATIVE AI PRACTICAL CRASH COURSE']):
        to_remove.append(b)

print(f"Blocks to remove from data-science-course: {len(to_remove)}")
for r in to_remove:
    txt = txt.replace(r, '')

# Also update the lead paragraph and module numbers in data-science-course
txt = txt.replace(
    'The curriculum begins with programming and data preparation, builds the mathematical foundations required for modelling, progresses through machine learning, deep learning, NLP, computer vision and ends with deployment and generative AI workflows.',
    'The curriculum provides complete end-to-end mastery over data preparation, business analytics, databases, statistics, machine learning algorithms, and real-world model deployment.'
)

with open('deployment_NeoNex/courses/data-science-course/index.html', 'w', encoding='utf-8') as f:
    f.write(txt)

print("Updated data-science-course: now strictly contains Data Science core modules!")

