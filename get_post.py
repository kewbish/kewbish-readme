from feedparser import parse

feed = parse("https://kewbish.github.io/blog/index.xml").entries
latest = f"[{feed[0].title}]({feed[0].link})\n{feed[0].published} - {feed[0].description}"

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
