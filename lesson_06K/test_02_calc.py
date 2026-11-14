import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("browser", ["chrome"])
def test_slow_calc(browser):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # === ЗАДЕРЖКА ===
    delay_input = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    # === КЛИКИ (кнопки — span) ===
    buttons = {
        "7": (By.XPATH, "//span[text()='7']"),
        "+": (By.XPATH, "//span[text()='+']"),
        "8": (By.XPATH, "//span[text()='8']"),
        "=": (By.XPATH, "//span[text()='=']"),
    }
    for text, locator in buttons.items():
        el = wait.until(EC.element_to_be_clickable(locator))
        el.click()

    # === РЕЗУЛЬТАТ (явное ожидание) ===
    result = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result
    driver.quit()
