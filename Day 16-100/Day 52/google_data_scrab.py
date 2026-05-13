from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


class GoogleDataScraper(object):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--incognito")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--disable-blink-features=AutomationControlMode")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        })
        self.wait = WebDriverWait(self.driver, 10)
        self.data = []

    def open_maps(self):
        self.driver.get("https://www.google.com/maps/?hl=en")
        time.sleep(5)

    def search(self, query):
        search_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search"]'))
        )
        search_button.click()
        time.sleep(1)

        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.click()
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

    def scroll_results(self):
        try:
            results_panel = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='feed']")))
        except:
            print("Results panel not found")
            return

        for _ in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                results_panel
            )
            time.sleep(2)

    def extract_data(self):
        places = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='article']")))

        for place in places:
            try:
                name = place.find_element(By.CSS_SELECTOR, "div.fontHeadlineSmall").text
            except:
                name = ""

            try:
                rating = place.find_element(By.CSS_SELECTOR, "span[aria-label*='stars']").get_attribute("aria-label")
            except:
                rating = ""

            try:
                link = place.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = ""

            self.data.append({
                "Name": name,
                "Rating": rating,
                "Link": link
            })

    def save_to_excel(self):
        df = pd.DataFrame(self.data)
        df.to_excel(r"C:\Users\stana\Desktop\google_data.xlsx", index=False)
        print(f"Saved {len(df)} records to google_data.xlsx!")

    def close(self):
        self.driver.quit()