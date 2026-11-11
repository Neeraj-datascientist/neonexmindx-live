import os

paths = [
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\generative-ai-engineering-course\index.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\generative-ai-engineering-course\index.html"
]

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = txt.replace(
            "<title>AI and Machine Learning Course India | NeoNex MindX</title>",
            "<title>Generative AI Course Online India | NeoNex MindX</title>"
        )
        txt = txt.replace(
            'content="AI and Machine Learning Course India | NeoNex MindX" property="og:title"',
            'content="Generative AI Course Online India | NeoNex MindX" property="og:title"'
        )
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"Updated title and OG title in {p}")

