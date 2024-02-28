from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="./Web-scraping/project/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "username"))
)

input_id = driver.find_element(By.ID, "username")
input_id.send_keys("XXXXXXX")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
)

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("XXXXXX" + Keys.ENTER)

menu = driver.find_element(By.CLASS_NAME, "NavPopInMenu")
menu.click()

time.sleep(50)
