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

"""we will try to get another info"""

#pattern = r"<label>Reference price |</label><strong class=\"f_Strong\">¥ <big>[0-9]+</big>\.?[0-9]*?<small class=\"hide-usd\">.*?</small></strong>"

pattern1 = r"¥ \d+"

matchResults1 = re.search(pattern1, html, re.IGNORECASE)
price1 = matchResults1.group()
price1 = re.sub("<.*?>", "", price1)
print(price1 )
