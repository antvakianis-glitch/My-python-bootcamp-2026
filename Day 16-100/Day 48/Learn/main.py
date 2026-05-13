from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text.strip(".")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is {price_dollar}.{price_cents}")

#driver.close()
driver.quit()