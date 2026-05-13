from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

def format_jobs(job_list):
    message = "New announcements for work:\n\n"
    for i, job in enumerate(job_list, 1):
        message += f"{i}. {job['title']}\n{job['link']}\n\n"
    return message

def send_email(job_list):
    sender = my_email
    receiver = my_email
    password = my_password

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = f"Infostud - {len(job_list)} new job ads"

    body = format_jobs(job_list)
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(sender, password)
        connection.sendmail(sender, receiver, msg.as_string())
        print(f"Email sent with {len(job_list)} announcements!")

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-save-password-bubble")

chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://poslovi.infostud.com/oglasi-za-posao?trigger_type=top_nav")


wait = WebDriverWait(driver, 10)

try:

    search_input = wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "input.ant-select-selection-search-input"
                ))
            )
    search_input.click()
    time.sleep(0.5)
    search_input.send_keys("python")
    time.sleep(1.5)
    search_input.send_keys(Keys.ESCAPE)


    city_input = driver.find_element(By.CSS_SELECTOR, "input#cities")
    city_input.send_keys("Novi Sad")
    time.sleep(1.5)
    city_input.send_keys(Keys.ENTER)
    city_input.send_keys(Keys.ESCAPE)

    cat_input = driver.find_element(By.CSS_SELECTOR, "input#categories")
    cat_input.send_keys("IT")
    time.sleep(1.5)
    cat_input.send_keys(Keys.ENTER)
    cat_input.send_keys(Keys.ESCAPE)


    search_btn = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[type='submit']"
        ))
    )
    search_btn.click()
    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.absolute.cursor-pointer")))
    job_cards = driver.find_elements(By.CSS_SELECTOR, "a.absolute.cursor-pointer")

    job_list = []

    if not job_cards:
        print("No jobs found")
    else:
        for card in job_cards:
            label_id = card.get_attribute("aria-labelledby")
            title_element = driver.find_element(By.ID, label_id)
            card_link = card.get_attribute("href")
            job_list.append({
                "title": title_element.text,
                "link": card_link
            })

    send_email(job_list)

except Exception as e:
    print(e)





