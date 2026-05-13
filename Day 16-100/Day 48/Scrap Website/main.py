import warnings
warnings.filterwarnings("ignore", message="Bad certificate in Windows certificate store")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.python.org/")
time.sleep(3)

event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")


event_dict = {
    date.get_attribute("datetime").split("T")[0]: event.text
    for date, event in zip(event_dates, event_names)
}

print(event_dict)



driver.close()