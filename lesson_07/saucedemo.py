from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username: str, password: str):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, product_id: str):
        self.wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
        self.wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(zip_code)

    def go_to_summary(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def get_total(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    