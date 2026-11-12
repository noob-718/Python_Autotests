from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def set_delay(self, seconds):
        input_field = self.wait.until(EC.presence_of_element_located((By.ID, "delay")))
        input_field.clear()
        input_field.send_keys(str(seconds))

    def click_number(self, number):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{number}']")))
        btn.click()

    def click_operator(self, operator):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{operator}']")))
        btn.click()

    def click_equals(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
        btn.click()

    def get_result(self):
        result = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
        return result.text.strip()
    