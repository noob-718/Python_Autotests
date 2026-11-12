from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    """Работа с текстовым полем и кнопкой (Task 2)."""
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")
        driver.implicitly_wait(10)

        # Поле custname
        name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "custname"))
        )
        name_field.clear()
        name_field.send_keys("Ivan")

        # Кнопка Submit
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]"))
        )
        submit_btn.click()

        # Проверяем, что URL изменился
        assert "/forms/post" in driver.current_url

    finally:
        driver.quit()
        