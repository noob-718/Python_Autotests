from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    """Проверка нескольких элементов (Task 3)."""
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")
        driver.implicitly_wait(10)

        # Все ссылки
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        # 1. Количество ссылок равно 9
        assert len(links) == 9, f"Expected 9 links, got {len(links)}"

        # 2. Все ссылки отображаются на странице
        for link in links:
            assert link.is_displayed(), "One or more links are not displayed"

        # 3. Текст первой ссылки содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, (
            f"Expected '1' in first link text, got '{first_link_text}'"
        )

    finally:
        driver.quit()
        