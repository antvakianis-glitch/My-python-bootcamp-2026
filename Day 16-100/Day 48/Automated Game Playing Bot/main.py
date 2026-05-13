import warnings
warnings.filterwarnings("ignore", message="Bad certificate in Windows certificate store")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

language_select = driver.find_element(By.CLASS_NAME, value="langSelectButton")
driver.execute_script("arguments[0].click();", language_select)
time.sleep(5)

input("Πάτα 'I am human' και μετά πάτα Enter εδώ...")

click_button = driver.find_element(By.ID, value="bigCookie")

def parse_cookies(text):
    text = text.split(" ")[0].replace(",", "")
    suffixes = {
        "million": 1_000_000,
        "billion": 1_000_000_000,
        "trillion": 1_000_000_000_000,
    }
    for suffix, multiplier in suffixes.items():
        if suffix in text:
            return int(float(text.replace(suffix, "")) * multiplier)
    return int(float(text))

def get_product_price(driver, product_id):
    try:
        product = driver.find_element(By.ID, value=product_id)
        price_elements = product.find_elements(By.CLASS_NAME, value="price")
        if not price_elements:
            return float("inf")
        price_text = price_elements[0].text.replace(",", "").strip()
        if not price_text:
            return float("inf")
        return int(float(price_text))
    except:
        return float("inf")

product_ids = [f"product{i}" for i in range(17, -1, -1)]

try:
    while True:
        driver.execute_script("arguments[0].click();", click_button)
        time.sleep(random.uniform(0.01, 0.05))

        cookies_text = driver.find_element(By.ID, value="cookies").text
        cookies_count = parse_cookies(cookies_text)
        print(f"Cookies: {cookies_count}")

        target_id = None
        target_price = 0

        for product_id in product_ids:
            try:
                elements = driver.find_elements(By.ID, value=product_id)
                if not elements:
                    continue
                product_class = elements[0].get_attribute("class")
                if "unlocked" not in product_class:
                    continue
                price = get_product_price(driver, product_id)
                if price == float("inf"):
                    continue
                if price > target_price:
                    target_price = price
                    target_id = product_id
            except:
                continue

        if target_id and cookies_count >= target_price:
            try:
                driver.find_elements(By.ID, value=target_id)[0].click()
                print(f">>> Bought {target_id} for {target_price:,} cookies")
            except:
                pass
        else:
            if target_id:
                print(f"--- Saving for {target_id} ({cookies_count}/{target_price})")

except KeyboardInterrupt:
    print("Bot σταμάτησε.")
    driver.quit()
