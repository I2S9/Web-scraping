from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./project/geckodriver.exe')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://cas.univ-paris13.fr/cas/login?service=https%3A%2F%2Fent.univ-paris13.fr')

username_input = driver.find_element(By.NAME, 'XXXXX')
password_input = driver.find_element(By.NAME, 'XXXXX')

username_input.send_keys('XXXXXX')
password_input.send_keys('XXXXXX')
password_input.send_keys(Keys.RETURN)

timeout = 10

try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id_on_next_page'))
    WebDriverWait(driver, timeout).until(element_present)
    print("Connexion réussie!")
except TimeoutException:
    print("Échec de la connexion. Assurez-vous que vos informations d'identification sont correctes.")

driver.quit()
