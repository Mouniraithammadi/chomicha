import requests
import bs4

urlBase = "https://www.choumicha.ma"


# html = requests.get("https://www.choumicha.ma/accueil-recettes/Page-14.html")
# soup = bs4.BeautifulSoup(html.text,'html.parser')
# divs = soup.findAll(class_="span4")

def getWajabatUrl(url):
    links = []
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    divs = soup.findAll(class_="span4")
    for div in divs:
        link = div.find("a").get("href")
        if link is not None:
            links.append(link)
    return links


def getInfoOfWajba(url):
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, "html.parser")
    data = {}
    data["url"] = url
    data["title"] = soup.find("h1", class_="fn").text
    recipe_info = soup.find("ul", class_="recipe-info").findAll("li")
    lis = {}
    for li in recipe_info:
        if li.find("strong") is not None  and  li.find("span") is not None:
            lis[str(li.find("strong").text).split(":")[0]] = li.find("span").text
    data["recipe-info"] = lis
    ingredients = soup.findAll(class_="ingredient")
    ingredients = [li.find("span" , class_="name").text for li in ingredients]
    data["ingredients"] = ingredients
    prepaDiv =  soup.find(class_="preparation").findAll("li")
    preparation = []
    for li in prepaDiv:
        preparation.append(str(li.get_text()))
    data["preparation"] = preparation
    data["categories"] = [a.get_text() for a in soup.select(".recette_divider li .row-fluid .row-fluid div a") if
                          a.get_text() != "Autres"]
    data["mots cles"] = [a.get_text() for a in soup.select(".recette_divider li .clearfix span a")]
    return data


u = 'https://www.choumicha.ma/recette/757-soupe-de-betteraves-au-fromage-de-chevre-a-la-ciboulette-batonnets-au-pavot.html'
# u = "https://www.choumicha.ma/c/tajines.html"
print(getInfoOfWajba(u))
