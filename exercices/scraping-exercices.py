import requests
from bs4 import BeautifulSoup
from pprint import pprint

# response = requests.get("https://www.google.com")

# print(response.text) Pour récupérer tout le code html de la page
# print(response.status_code) Permet de vérfier si on a une error de code (erreur 404 par exemple)
# print(response.raise_for_status()) Permet de lever une erreur dans le cas où on a un pb dans la requête, ici renvoie 'None' car pas de pb dans l'URL

# with open('index.html', 'w') as f:
#     f.write(response.text)


# soup = BeautifulSoup(response.text, 'html.parser') # parser html très rapide #html5lib si page complexe

# # print(soup.prettify()) # affiche l'ensemble du code html indenté = plus facile à lire


# images = soup.find_all('article', class_ = "product_pod")  # find retourne un seul élément et find_all retourne tjr une liste

# pprint(images)

# aside = soup.find('aside')
# for child in aside.children:
#     if child.name:
#         print(child.name)

# side_categories = aside.find('div', class_ = 'side_categories')

# print(side_categories)

# links = side_categories.find_all('a')

# pprint(links)

# print(aside.parent.parent.parent)  # fonctionnalités de récursivité pour naviguer 

url = "http://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

aside = soup.find('div', class_ = "side_categories")

print(aside)

categories_div = aside.find("ul").find('li').find('ul')

categories = [child.text.strip() for child in categories_div.children if child.name]

# On récupère le texte de toutes les catégories du site

# for category in categories.children:
#     # print(category.text.strip()) # la méthode strip() permet de retirer les espaces (excepté les objets 'None')
#     # on écrit donc :
#     if category.name:
#         print(category.text.strip())

pprint(categories)

images = soup.find('section').find_all('img')

for image in images:
    print(image['src'])

    