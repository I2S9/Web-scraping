from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="./Web-scraping/project/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr")

input_id = driver.find_element(By.ID, "username")
input_id.send_keys("XXXXX")

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("XXXX" + Keys.ENTER)

