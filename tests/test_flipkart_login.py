import os

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


FLIPKART_URL = "https://www.flipkart.com/"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()


def test_open_login_and_enter_username(driver):
    username = os.getenv("FLIPKART_USERNAME")
    if not username:
        pytest.skip("Set FLIPKART_USERNAME to a test mobile number or email")

    wait = WebDriverWait(driver, 15)
    driver.get(FLIPKART_URL)

    # Flipkart changes its UI periodically, so try common login entry points.
    login_selectors = [
        (By.XPATH, "//a[contains(., 'Login')]"),
        (By.XPATH, "//span[normalize-space()='Login']"),
        (By.XPATH, "//button[contains(., 'Login')]"),
    ]

    for selector in login_selectors:
        try:
            wait.until(EC.element_to_be_clickable(selector)).click()
            break
        except TimeoutException:
            continue

    username_field = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[type='text'], input[type='email'], input[type='tel']",
            )
        )
    )
    username_field.clear()
    username_field.send_keys(username)

    assert username_field.get_attribute("value") == username

    # Intentionally stop here. Complete OTP/CAPTCHA manually; do not automate bypasses.
