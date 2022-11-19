import re
from urllib.request import urlopen

url = 'https://buff.163.com/goods/35282#tab=price-chart'

page = urlopen(url)

print(page)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

#print(html)

titleIndex = html.find("<title>")
startIndex = titleIndex + len("<title>")

print(startIndex)
print(titleIndex)

endIndex = html.find("</title>")

title = html[startIndex:endIndex]

print(title)

print("-----------------------------")

pattern = "<title.*?>.*?</title.*?>"

matchResults = re.search(pattern, html, re.IGNORECASE)
title = matchResults.group()
title = re.sub("<.*?>", "", title)

print(title)

