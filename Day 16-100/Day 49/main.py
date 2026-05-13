import warnings

warnings.filterwarnings("ignore", message="Bad certificate in Windows certificate store")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta, date

ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"

#user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument(f"user-data-dir={user_data_dir}")
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

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, 20)

join_today = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Home_heroButton__3eeI3")))
join_today.click()

email_input =wait.until(EC.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, value="password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit = driver.find_element(By.ID, value="submit-button")
submit.click()

class_schedule = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='scheduleTitle']")))
today = datetime.today()

days_until_tuesday = (1 - today.weekday()) % 7
days_until_thursday = (3 - today.weekday()) % 7

next_tuesday = today + timedelta(days=days_until_tuesday)
next_thursday = today + timedelta(days=days_until_thursday)

target_dates = [
    next_tuesday.strftime("%Y-%m-%d"),   # "2026-03-31"
    next_thursday.strftime("%Y-%m-%d"),  # "2026-04-02"
]

target_date_strs = [
    next_tuesday.strftime("%b") + " " + str(next_tuesday.day),   # "Mar 31"
    next_thursday.strftime("%b") + " " + str(next_thursday.day), # "Apr 2"
]

already_count = 0

day_groups = driver.find_elements(By.CSS_SELECTOR, "[id^='day-group']")

booked_classes = []
waitlist_classes = []

for day_group in day_groups:
    day_title = day_group.find_element(By.CSS_SELECTOR, "[id^='day-title']").text

    if any(target in day_title for target in target_date_strs):
        buttons_6pm = day_group.find_elements(By.CSS_SELECTOR, "[id$='-1800']")

        for button in buttons_6pm:
            button_id = button.get_attribute("id")
            class_name = button_id.split("-")[2].capitalize()
            button_text = button.text

            if button_text == "Book Class":
                button.click()
                booked_classes.append(f"{class_name} on {day_title}")
            elif button_text == "Join Waitlist":
                button.click()
                waitlist_classes.append(f"{class_name} on {day_title}")
            elif button_text in ("Booked", "Waitlisted"):
                already_count += 1

print("\n--- BOOKING SUMMARY ---")
for c in booked_classes:
    print(f"  ✅ Booked: {c} at 6:00 PM")
for c in waitlist_classes:
    print(f"  ⏳ Waitlisted: {c} at 6:00 PM")
print(f"\nNew bookings: {len(booked_classes)}")
print(f"New waitlist entries: {len(waitlist_classes)}")
print(f"Already handled: {already_count}")

my_bookings_link = wait.until(EC.presence_of_element_located((By.ID, "my-bookings-link")))
my_bookings_link.click()

expected = len(booked_classes) + len(waitlist_classes) + already_count

print(f"\n--- Total Tuesday/Thursday 6pm classes: {expected} ---")

print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

verified = []

booking_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[id^='booking-card']")))

for card in booking_cards:
    when_el = card.find_element(By.XPATH, ".//p[contains(., 'When:')]")
    when_text = when_el.text

    if "6:00 PM" not in when_text:
        continue
    try:
        date_part = when_text.replace("When: ", "").split(",")[0:2]
        date_str = ",".join(date_part).strip()  # "Thu, Apr 2"
        parsed_date = datetime.strptime(date_str + f" {datetime.today().year}", "%a, %b %d %Y").date()
    except ValueError:
        continue

    if parsed_date not in [next_tuesday.date(), next_thursday.date()]:
        continue

    name_el = card.find_element(By.CSS_SELECTOR, "[id^='booking-class-name']")
    class_name = name_el.text
    status = card.get_attribute("data-booking-status")

    if status == "waitlisted":
        print(f"  ✓ Verified: {class_name} (Waitlist)")
        verified.append(f"{class_name} (Waitlist)")
    else:
        print(f"  ✓ Verified: {class_name}")
        verified.append(class_name)

# --- Verification Result ---
found = len(verified)
diff = expected - found
booking_word_expected = "booking" if expected == 1 else "bookings"
booking_word_found = "booking" if found == 1 else "bookings"

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {expected} {booking_word_expected}")
print(f"Found: {found} {booking_word_found}")

if diff == 0:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {diff} {booking_word_expected}")


#driver.quit()