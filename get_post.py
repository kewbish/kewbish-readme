from feedparser import parse

feed = parse("https://kewbish.github.io/blog/index.xml").entries
latest = f"""
<div style="border: 1px solid; border-radius: 5px; padding: 0.5% 1%; width: 50%;">
\n<h3><a href="{feed[0].link}">{feed[0].title} 🖋️</a></h3>\n
<p>{feed[0].description} - <small>{feed[0].published}</small></p>\n</div>"""

farr = []
with open("README.md", "r", encoding='utf8') as x:
    for line in x:
        if line.strip() == "<!--bp-->":
            break
        farr.append(line)

with open("README.md", "w", encoding='utf8') as x:
    x.writelines(farr)
    x.write("<!--bp-->\n")
    x.write(latest)
