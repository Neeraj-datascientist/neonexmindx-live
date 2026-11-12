import re

txt = open('deployment_NeoNex/courses/data-science-and-ai-course/index.html', 'r', encoding='utf-8').read()

print("Title:", re.search(r'<title>(.*?)</title>', txt).group(1))
print("H1:", re.search(r'<h1.*?>(.*?)</h1>', txt, re.DOTALL).group(1).strip())

# Check syllabus links
syls = set(re.findall(r'href=[\"\']([^\"\']*data-science[^\"\']*)[\"\']', txt))
print("Syllabus / DS links in data-science-and-ai-course:")
for s in syls:
    print("  ", s)

