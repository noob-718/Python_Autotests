from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def test_dynamic_loading():
   
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Нажимаем кнопку "Start" (CSS-селектор)
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Явное ожидание появления текста "Hello World!"
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#finish"), "Hello World!")
        )

        # 4. Скриншот страницы
        driver.save_screenshot("lesson06_task1_screenshot.png")

        # 5. Проверяем текст
        finish_text = driver.find_element(By.CSS_SELECTOR, "#finish").text
        assert finish_text == "Hello World!", f"Ожидался 'Hello World!', получено: {finish_text}"

        print("✅ Task 1 пройден успешно!")

    except TimeoutException:
        print("❌ Ошибка: текст 'Hello World!' не появился в течение 10 секунд")
        raise
    except AssertionError as e:
        print("❌ Проверка текста не прошла")
        raise
    finally:
        driver.quit()
