from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    """Навигация и проверка URL (Task 1)."""
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.qa-territory.online")
        driver.implicitly_wait(10)

        # Кликаем по ссылке "HTML Form"
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form"))
        )
        link.click()

        # Проверяем новый URL
        assert "/forms/post" in driver.current_url

        # Возвращаемся назад
        driver.back()

        # Проверяем, что вернулись на исходный URL
        assert driver.current_url == "https://httpbin.qa-territory.online/"

    finally:
        driver.quit()
        