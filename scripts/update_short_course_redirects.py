import re

redirects_path = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\_redirects"
with open(redirects_path, "r", encoding="utf-8") as f:
    txt = f.read()

# Lines to remove:
unwanted_rules = [
    "/courses/sql-course                      /courses/data-analytics-course/         301!",
    "/courses/sql-course/                     /courses/data-analytics-course/         301!",
    "/courses/excel-power-bi-tableau-course   /courses/data-analytics-course/         301!",
    "/courses/excel-power-bi-tableau-course/  /courses/data-analytics-course/         301!",
    "/courses/python-programming-course       /courses/data-science-course/           301!",
    "/courses/python-programming-course/      /courses/data-science-course/           301!",
    "/courses/machine-learning-course         /courses/ai-ml-course/                  301!",
    "/courses/machine-learning-course/        /courses/ai-ml-course/                  301!",
    "/Neonex*Excel*PowerBI*Tableau*Course*    /courses/data-analytics-course/          301!",
    "/Neonex*Machine*Learning*Course*         /courses/ai-ml-course/                   301!",
    "/Neonex*Python*Programming*Course*       /courses/data-science-course/            301!",
    "/Neonex*SQL*Course*                      /courses/data-analytics-course/          301!",
    "/Neonex%20Mindx%20Excel%20PowerBI%20Tableau%20Course.html /courses/data-analytics-course/ 301!",
    "/Neonex%20Mindx%20Excel%20PowerBI%20Tableau%20Course /courses/data-analytics-course/ 301!",
    "/Neonex%20Mindx%20Python%20Programming%20Course.html /courses/data-science-course/ 301!",
    "/Neonex%20Mindx%20Python%20Programming%20Course /courses/data-science-course/ 301!",
    "/Neonex%20Mindx%20SQL%20Course.html      /courses/data-analytics-course/ 301!",
    "/Neonex%20Mindx%20SQL%20Course           /courses/data-analytics-course/ 301!"
]

new_txt = txt
for r in unwanted_rules:
    new_txt = new_txt.replace(r, "")

# Now add clean canonical redirects for their legacy naming
clean_mappings = """
# 4 SHORT COURSES CLEAN DIRECTORIES (Now live standalone pages!)
/courses/python-programming-course      /courses/python-programming-course/     301!
/courses/excel-power-bi-tableau-course  /courses/excel-power-bi-tableau-course/ 301!
/courses/sql-course                     /courses/sql-course/                    301!
/courses/machine-learning-course        /courses/machine-learning-course/       301!

/python-programming-course              /courses/python-programming-course/     301!
/python-programming-course/             /courses/python-programming-course/     301!
/excel-power-bi-tableau-course          /courses/excel-power-bi-tableau-course/ 301!
/excel-power-bi-tableau-course/         /courses/excel-power-bi-tableau-course/ 301!
/sql-course                             /courses/sql-course/                    301!
/sql-course/                            /courses/sql-course/                    301!
/machine-learning-course                /courses/machine-learning-course/       301!
/machine-learning-course/               /courses/machine-learning-course/       301!

/Neonex*Excel*PowerBI*Tableau*Course*   /courses/excel-power-bi-tableau-course/ 301!
/Neonex*Machine*Learning*Course*        /courses/machine-learning-course/       301!
/Neonex*Python*Programming*Course*      /courses/python-programming-course/     301!
/Neonex*SQL*Course*                     /courses/sql-course/                    301!
"""

# Replace top comment block
new_txt = re.sub(r'# 301 Permanent Redirects for standalone tool courses -> Main Program.*?(?=# Cloudflare Pages Clean Canonical Redirects)', clean_mappings.strip() + '\n\n', new_txt, flags=re.S)

with open(redirects_path, "w", encoding="utf-8") as f:
    f.write(new_txt)

print("Updated _redirects so short courses load their own standalone pages directly!")

