from lxml import html
import requests


# k = r''

newList = [] # LISTA COM OS LINKS

pageF = requests.get(k)
treeF = html.fromstring(pageF.content)

mlSites = treeF.xpath("//a[@class = 'item-link item__js-link']")

for j in mlSites:
    newList.append(j.attrib['href'])

precoFloat = []

for i in newList:
    print(i)
    page = requests.get(i)
    tree = html.fromstring(page.content)

    precoAdquirido = tree.xpath("//span[@class = 'price-tag-fraction']/text()")
    cents = tree.xpath("//span[@class = 'price-tag-cents-visible']/text()")


    if not cents:
        cents = tree.xpath("//span[@class = 'price-tag-cents']/text()") or [0]

    precoFloat = int(str(precoAdquirido[0]).replace('.', ''))

    precoAdquirido = precoFloat + (int(cents[0]) / 100)
    print(precoAdquirido)