import requests
from bs4 import BeautifulSoup

login_url = 'https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr'

payload = {
    'username': 'XXXXXXXX',
    'password': 'XXXXXXXX'
}

response = requests.post(login_url, data=payload)

if response.status_code == 200:
    print("Connexion réussie!")
else:
    print(f"Échec de la connexion avec le code d'état : {response.status_code}")
    print("Assurez-vous que vos informations d'identification sont correctes.")

# class "mailbox inbox selected unread", classe supposée pour lire les messages non lus
