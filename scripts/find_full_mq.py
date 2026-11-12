import re

b = 'deployment_NeoNex/blog-post.html'
txt = open(b, 'r', encoding='utf-8').read()

m = re.search(r'@media \(max-width:\s*1024px\)\s*\{.*?\}', txt, re.DOTALL)
if m:
    start = m.start()
    # find where this media block ends
    open_b = 0
    end = start
    for i in range(start, len(txt)):
        if txt[i] == '{':
            open_b += 1
        elif txt[i] == '}':
            open_b -= 1
            if open_b == 0:
                end = i + 1
                break
    print(txt[start:end])

