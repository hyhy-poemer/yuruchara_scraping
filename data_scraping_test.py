import re
from html import unescape 

with open('dp.html') as f:
    html = f.read()

for partial_html in re.findall(r'<a intemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
    url = re.search(r'<a intemprop="url" href="(.*?)">', partial_html).group(1)
    url = 'https://gihyo.jp' + url

    title = re.search(r'<p intemprop="name".*?</p>', partial_html).group(0)
    title = title.replace('<br/>', ' ')
    title = re.sub(r'<.*?>', '', title)
    title = unescape(title)

    print(url, title)