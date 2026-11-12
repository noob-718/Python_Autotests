import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("browser", ["edge", "safari"])
def test_form(browser):
    # === ДРАЙВЕР (только явные ожидания) ===
    options = webdriver.EdgeOptions() if browser == "edge" else webdriver.SafariOptions()
    driver = webdriver.Edge() if browser == "edge" else webdriver.Safari()
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # === ЗАПОЛНЕНИЕ ФОРМЫ (только name) ===
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone-number": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
        "zip-code": ""  # пустое поле
    }

    for key, value in fields.items():
        el = wait.until(EC.presence_of_element_located((By.NAME, key)))
        el.clear()
        el.send_keys(value)

    # === ОТПРАВКА ===
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
    submit.click()

    # === ПРОВЕРКА ЦВЕТА ПОЛЕЙ (только явные ожидания) ===
    zip_el = wait.until(EC.presence_of_element_located((By.ID, "zipCode")))
    zip_color = driver.execute_script(
        "return getComputedStyle(arguments[0]).getPropertyValue('border-color');", zip_el
    )
    assert zip_color in ["rgb(255, 0, 0)", "#ff0000"], f"Zip code должен быть красным, а не {zip_color}"

    green = ["rgb(34, 197, 94)", "#22c55e"]
    for key in fields.keys():
        if key == "zip-code":
            continue
        el = wait.until(EC.presence_of_element_located((By.ID, key)))
        color = driver.execute_script(
            "return getComputedStyle(arguments[0]).getPropertyValue('border-color');", el
        )
        assert color in green, f"Поле {key} должно быть зелёным, а не {color}"

    driver.quit()
    