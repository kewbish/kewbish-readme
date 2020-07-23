from feedparser import parse

feed = parse("https://kewbish.github.io/blog/index.xml").entries
latest = f"[{feed[0].title}]({feed[0].link})\n{feed[0].published} - {feed[0].description}"
print(latest)
