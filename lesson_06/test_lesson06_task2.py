from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_session_storage_auth():

    driver = webdriver.Chrome()

    try:
        # === АККАУНТ 1 ===
        driver.get("https://gitflic.ru/")
        driver.add_cookie({
            "name": "SESSION",
            "value": "NzA3ZDg1OTYtNGRmNS00MGUxLWIxYmUtZTU5MWM1NjkyNzVk",
            "domain": "gitflic.ru",
            "path": "/",
            "secure": False,
            "sameSite": "Lax"
        })
        driver.refresh()

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.url_contains("user1")
        )
        url_user1 = driver.current_url
        print(f"✅ URL аккаунта 1: {url_user1}")

        # === ЛОГИН 1 ===
        driver.delete_all_cookies()

        # === АККАУНТ 2 ===
        driver.get("https://gitflic.ru/")
        driver.add_cookie({
            "name": "SESSION",
            "value": "OWI5YzE1NTQtODg5Mi00MjllLTg0MTYtYjZlMTczZDJjMTI4",
            "domain": "gitflic.ru",
            "path": "/",
            "secure": False,
            "sameSite": "Lax"
        })
        driver.refresh()

        wait.until(
            EC.url_contains("user2")
        )
        url_user2 = driver.current_url
        print(f"✅ URL аккаунта 2: {url_user2}")

        # Проверка, что URL различаются
        assert url_user1 != url_user2

        print("✅ Task 2 пройден успешно! URL аккаунтов разные.")

    except TimeoutException:
        print("❌ Ошибка: не удалось дождаться перехода на страницу пользователя")
        raise
    except AssertionError as e:
        print("❌ Проверка URL не прошла")
        raise
    finally:
        driver.quit()
