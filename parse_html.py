from bs4 import BeautifulSoup

f = open('index.html', 'r')
html_doc = f.read()
f.close()

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())

print soup.title
# <title>The Dormouse's story</title>

print soup.title.name
# u'title'

print soup.title.string
# u'The Dormouse's story'

print soup.title.parent.name
# u'head'

print soup.p
# <p class="title"><b>The Dormouse's story</b></p>

print soup.p['class']
# u'title'

print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print soup.find(id="link3")

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())
