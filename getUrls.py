import requests
import bs4

ToArray = lambda name, rng: [f"https://www.choumicha.ma/c/{name.replace('.html', f'')}/Page-{str(index + 1)}.html" for
                             index in range(rng)]
urls = []


def checkD(text: str) -> bool:
    for chr in text:
        if chr.isdigit():
            return True
    return False


def getN(text: str) -> int:
    text = text.split("/")[-1].replace(".html", "")
    n = 0
    ten = 1
    for chr in text:
        if chr.isdigit():
            n = 10 * n + int(chr)
    return n


def getFin(url: str) -> int:
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    ul = soup.find(class_="pagination-end")
    if ul is None:
        return None
    return getN(ul.find("a").get("href"))


def getBaseUrls():
    html = requests.get("https://www.choumicha.ma/c/gateaux-marocains/Page-5.html")
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    ul = soup.find(class_="level1")
    global urls
    li = ul.findAll("li")
    for i in li:
        u = str(i.find("a").get("href")).split("/")[-1].replace(".html", "")
        if checkD(u):
            urls.append(f'https://www.choumicha.ma{i.find("a").get("href")}')
        else:
            numberOfWajabat = getFin(f'https://www.choumicha.ma{i.find("a").get("href")}')
            if numberOfWajabat is None:
                urls.append(i.find("a").get("href"))
                continue
            urls += ToArray(u, numberOfWajabat)

getBaseUrls()
for  u in urls:
    print(u)

