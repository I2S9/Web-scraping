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
input_id.send_keys("XXXXXX")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
)

input_password = driver.find_element(By.ID, "password")
input_password.send_keys("XXXXXX" + Keys.ENTER)

menu = driver.find_element(By.CLASS_NAME, "NavPopInMenu")
menu.click()

time.sleep(10)

mail = driver.find_element(By.CLASS_NAME, "wdg_mn_li_webmail")
mail.click()

time.sleep(10)

unread_mails = []

message_rows = driver.find_elements(By.XPATH, './/tbody//tr[contains(@class, "message unread")]')

for message_row in message_rows:
    sender = message_row.find_element(By.CLASS_NAME, 'fromto').text
    subject = message_row.find_element(By.CLASS_NAME, 'subject').text
    date = message_row.find_element(By.CLASS_NAME, 'date').text
    unread_mails.append([subject, sender, date])

for index, message_row in enumerate(message_rows):
    sender = message_row.find_element(By.CLASS_NAME, 'fromto').text
    subject = message_row.find_element(By.CLASS_NAME, 'subject').text
    date = message_row.find_element(By.CLASS_NAME, 'date').text
    unread_mails.append([subject, sender, date])


for index, mail in enumerate(unread_mails):
    print(f"Objet: {mail[0]}\nExpéditeur: {mail[1]}\nDate: {mail[2]}")

    message_rows[index].click()
    driver.implicitly_wait(50)
    mail_content = driver.find_element(By.CLASS_NAME, 'contenu_class').text
    print(f"Contenu du mail: {mail_content}")
    driver.back()
    time.sleep(50) 

# message_rows = driver.find_elements(By.XPATH, './/tbody//tr[contains(@class, "message unread")]')

# # print(message_rows)


# time.sleep(50)

# for message_row in message_rows:
#     sender = message_row.find_element(By.CLASS_NAME, 'fromto').text
#     subject = message_row.find_element(By.CLASS_NAME, 'subject').text
#     date = message_row.find_element(By.CLASS_NAME, 'date').text
#     unread_mails.append([subject, sender, date])

# for index, message_row in enumerate(message_rows):
#     sender = message_row.find_element(By.CLASS_NAME, 'fromto').text
#     subject = message_row.find_element(By.CLASS_NAME, 'subject').text
#     date = message_row.find_element(By.CLASS_NAME, 'date').text
#     unread_mails.append([subject, sender, date])

# for index, mail in enumerate(unread_mails):
#     print(f"Objet: {mail[0]}\nExpéditeur: {mail[1]}\nDate: {mail[2]}")

#     message_rows[index].click()
#     driver.implicitly_wait(50)
#     mail_content = driver.find_element(By.CLASS_NAME, 'contenu_class').text
#     print(f"Contenu du mail: {mail_content}")
#     driver.back()
#     time.sleep(50) 

