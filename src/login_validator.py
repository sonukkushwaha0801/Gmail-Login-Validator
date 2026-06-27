import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import LOGIN_URL, WAIT_TIME


def login_account(email, password):  # Attempt to log in to a Gmail account using Selenium and return the result
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium"

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    print("Starting browser...")
    driver = webdriver.Chrome(options=chrome_options)
    print("Browser started successfully")
    # driver = webdriver.Chrome()

    try:
        driver.fullscreen_window()
        driver.get(LOGIN_URL)

        current_page = driver.current_url

        # Email Input
        email_box = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_box.send_keys(email + Keys.ENTER)

        # Password Input
        try:
            password_box = WebDriverWait(driver, WAIT_TIME).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
                )
            )
            password_box.send_keys(password + Keys.ENTER)
            time.sleep(5)
        except Exception as e:
            return False, f"Incorrect Email"

        # Wait for login result
        try:
            WebDriverWait(driver, 20).until(
                lambda d: "mail.google.com" in d.current_url
            )

            driver.find_element(By.XPATH, '//a[contains(@href,"SignOutOptions")]')
            return True, "Login Successful"

        except Exception as e:
            return False, f"Login Failed: {str(e)}"

    finally:
        driver.quit()


if __name__ == "__main__":
    email = "test001004@collegename.in"
    password = "test001004"

    status, message = login_account(email, password)
    print(status, message)
