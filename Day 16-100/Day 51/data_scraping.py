from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.download_speed = 0
        self.upload_speed = 0
        self.driver = None
        self.wait = None

    def get_connection(self):
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net/")

        self.wait = WebDriverWait(self.driver, 20)


        go_button = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                ".start-button a"
            ))
        )

        go_button.click()

    def get_speeds(self):
        import time

        try:
            time.sleep(45)

            download = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
            upload = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

            self.download_speed = float(download)
            self.upload_speed = float(upload)

            print(self.download_speed, self.upload_speed)
            return self.download_speed, self.upload_speed


        except Exception as e:

            print("Retrying...", e)

            time.sleep(10)

            download = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text

            upload = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

            self.download_speed = float(download)

            self.upload_speed = float(upload)

            return self.download_speed, self.upload_speed

    def check_speed_and_notify(self):
        if float(self.download_speed) < 50:
            print("Internet is slow → sending email")
            self.send_email()
        else:
            print("Internet OK")

    def send_email(self):

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg=f"Subject: Internet Speed Check Alert\r\n\r\nThe current download speed is {self.download_speed} Mbps.\r\nThe current upload speed is {self.upload_speed} Mbps.\r\n")
            print("Email sent!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Check your email/app password.")
        except smtplib.SMTPException as e:
            print(f"Email error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")












