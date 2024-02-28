import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# Login address to my ENT (Digital Work Environment)

login_url = 'https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr'

# ID & passwords 

payload = {
    'username': 'XXXXX',
    'password': 'XXXXXX'
}

response = requests.post(login_url, data=payload)

# Check if the connexion works

if response.status_code == 200:
    print("Connexion réussie!")
else:
    print(f"Échec de la connexion avec le code d'état : {response.status_code}")
    print("Assurez-vous que vos informations d'identification sont correctes.")


# class "mailbox inbox selected unread", classe supposée pour lire les messages non lus

# On a une seconde classe "unreadcount" qui permet de dénombrer le nombre de messages non lus

# On a 'div id = 'messagelistcontainer' class = "boxlistcontent"
    # Sous classe = enfant "records-table shortheader" 
        # on a accès à tous les messages avec pour id = 'rcmrowXXX' et pour classe deux options :
            # "message unread selected focused" pour les messages non lus
            # "message" pour les mails lus


# On souhaite recueillir trois informations principales 

# 1. qui a envoyé le mail : pour cela on a une classe "fromto"
# 2. l'objet = via la classe "subject"
# 3. la date avec la classe "date"
    
# Après on a d'autres infos comme la taille du mail, les pièces jointes etc.. 
    # pièce jointe dans "attachment"

