from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ZillowFiller:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.URL = "https://appbrewery.github.io/Zillow-Clone/"
        self.response = requests.get(self.URL, headers=self.headers)

        self.driver = webdriver.Chrome()
        self.FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeBG5rxl6mFNezpxugoDZplcIiIVaRmzgxoI17ndyYSQZn82w/viewform"

        self.all_links = []
        self.all_prices = []
        self.all_addresses = []

    def get_listings(self):
        soup = BeautifulSoup(self.response.content, "html.parser")

        all_link_elements = soup.select(".property-card-link")
        self.all_links = [item["href"] for item in all_link_elements]

        all_price_elements = soup.select(".PropertyCardWrapper__StyledPriceLine")
        self.all_prices = [item.get_text(strip=True).replace("/mo", "").split("+")[0] for item in
                           all_price_elements]
        all_address_elements = soup.select("[data-test='property-card-addr']")
        self.all_addresses = [item.get_text(strip=True) for item in all_address_elements]

        return self.all_links, self.all_prices, self.all_addresses

    def fill_form(self, address, price, link):
        self.driver.get(self.FORM_URL)
        time.sleep(2)

        inputs = self.driver.find_elements(By.CLASS_NAME, "zHQkBf")
        inputs[0].send_keys(address)
        inputs[1].send_keys(price)
        inputs[2].send_keys(link)

        submit_button = self.driver.find_element(By.XPATH, "//span[text()='Submit']")
        submit_button.click()
        time.sleep(1)