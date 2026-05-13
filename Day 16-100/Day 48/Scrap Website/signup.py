import warnings
warnings.filterwarnings("ignore", message="Bad certificate in Windows certificate store")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

load_dotenv()

f_name = os.getenv("F_NAME")
l_name = os.getenv("L_NAME")
email = os.getenv("EMAIL")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
time.sleep(3)

search_firstname = driver.find_element(By.NAME, value="fName")
search_lastname = driver.find_element(By.NAME, value="lName")
search_email = driver.find_element(By.NAME, value="email")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

search_firstname.send_keys(f_name)
search_lastname.send_keys(l_name)
search_email.send_keys(email)


sign_up_button.click()

driver.close()


