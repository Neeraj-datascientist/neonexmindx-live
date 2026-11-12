import re

# In courses/data-science-course/index.html
ds_path = 'deployment_NeoNex/courses/data-science-course/index.html'
txt_ds = open(ds_path, 'r', encoding='utf-8').read()

# Only keep Data Science info in the summary table
old_duration_ds = '<td>9&ndash;11 months (Data Science) | 10&ndash;11 months (Data Science & AI)</td>'
new_duration_ds = '<td>9&ndash;11 Months</td>'
txt_ds = txt_ds.replace(old_duration_ds, new_duration_ds)

old_fee_ds = '<td>₹65,000 (Data Science) | ₹75,000 (Data Science & AI)</td>'
new_fee_ds = '<td>₹65,000</td>'
txt_ds = txt_ds.replace(old_fee_ds, new_fee_ds)

with open(ds_path, 'w', encoding='utf-8') as f:
    f.write(txt_ds)
print("Updated data-science-course summary table cleanly!")

# In courses/data-science-and-ai-course/index.html
ds_ai_path = 'deployment_NeoNex/courses/data-science-and-ai-course/index.html'
txt_ai = open(ds_ai_path, 'r', encoding='utf-8').read()

new_duration_ai = '<td>10&ndash;11 Months</td>'
txt_ai = txt_ai.replace(old_duration_ds, new_duration_ai)

new_fee_ai = '<td>₹75,000</td>'
txt_ai = txt_ai.replace(old_fee_ds, new_fee_ai)

# Update core learning row in data-science-and-ai-course
old_core = '<td>Python, SQL, statistics, probability, linear algebra, machine learning and deployment</td>'
new_core = '<td>Python, SQL, MongoDB, Power BI, Tableau, Excel, statistics, ML, Deep Learning, NLP, Computer Vision, MLOps, AWS and Generative AI Practical Crash Course</td>'
txt_ai = txt_ai.replace(old_core, new_core)

# Update hero points in data-science-and-ai-course
txt_ai = txt_ai.replace('Structured 6&ndash;7 month learning path', 'Structured 10&ndash;11 month learning path')

with open(ds_ai_path, 'w', encoding='utf-8') as f:
    f.write(txt_ai)
print("Updated data-science-and-ai-course summary table and hero points cleanly!")

