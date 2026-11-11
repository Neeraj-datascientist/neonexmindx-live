import glob
import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
html_files = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)

# Replacements map:
REPLACEMENTS = {
    # contact-us (187 -> 149)
    "Contact NeoNex MindX for course counselling, syllabus, fees, batch timings and enrolment support for Data Analytics, Data Science, AI/ML, Data Engineering and Business Analytics programs.":
    "Contact NeoNex MindX for course counselling, syllabus details, batch timings and enrolment support across our Data Analytics, Data Science and AI programs.",
    
    # blogs (181 -> 148)
    "Read practical tutorials, roadmaps, tool guides and career transition advice across Data Analytics, Data Science, AI/ML, Data Engineering and Business Analytics from the NeoNex MindX team.":
    "Read practical tutorials, roadmaps, tool guides and career advice across Data Analytics, Data Science, AI/ML and Data Engineering from NeoNex MindX.",
    
    # privacy-policy (175 -> 147)
    "Read how NeoNex MindX collects, uses and protects learner and visitor information, including analytics, communications, cookies and data privacy rights under applicable law.":
    "Read how NeoNex MindX collects, uses and protects learner data, including communications, cookies and data privacy rights under applicable regulations.",
    
    # terms-and-conditions (178 -> 147)
    "Read the terms and conditions governing enrollment, course delivery, payments, platform usage, intellectual property and policies for NeoNex MindX programs and short courses.":
    "Read the terms governing enrollment, live course delivery, payments, learning platform usage and code of conduct for NeoNex MindX career programs.",
    
    # refund-and-cancellation-policy (185 -> 146)
    "Read the NeoNex MindX policy on batch changes, pause requests, withdrawals, refund eligibility and conditions applicable to live online programs and focused short courses.":
    "Read the NeoNex MindX policy on batch transfers, program pauses, withdrawal windows and refund terms applicable to our live online training tracks.",
    
    # placement-assistance-disclaimer (187 -> 147)
    "Read NeoNex MindX career support scope: interview prep, portfolio review, mock interviews and job search readiness. NeoNex MindX does not provide an unconditional job guarantee.":
    "Read NeoNex MindX career support scope: interview prep, portfolio reviews and mock sessions. NeoNex MindX provides career assistance, not a job guarantee."
}

count = 0
for f in html_files:
    if any(k in f.lower() for k in [".git", "savepoints", "cms", "admin", "node_modules"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
    new_txt = txt
    for old_s, new_s in REPLACEMENTS.items():
        if old_s in new_txt:
            new_txt = new_txt.replace(old_s, new_s)
    if new_txt != txt:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_txt)
        count += 1

print(f"Updated meta descriptions across {count} files.")