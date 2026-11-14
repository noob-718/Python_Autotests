import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("browser", ["firefox"])
def test_shop(browser):
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # === АВТОРИЗАЦИЯ ===
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(
        "standard_user"
    )
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(
        "secret_sauce"
    )
    driver.find_element(By.ID, "login-button").click()

    # === ДОБАВЛЕНИЕ ТОВАРОВ (точные id кнопок) ===
    products = [
        ("Sauce Labs Backpack", "add-to-cart-sauce-labs-backpack"),
        ("Sauce Labs Bolt T-Shirt", "add-to-cart-sauce-labs-bolt-t-shirt"),
        ("Sauce Labs Onesie", "add-to-cart-sauce-labs-onesie"),
    ]
    for _, product_id in products:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    # === КОРЗИНА ===
    cart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart.click()

    # === CHECKOUT ===
    checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout.click()

    # === ДАННЫЕ ===
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Петров")
    wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(
        "123456"
    )

    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # === ИТОГОВАЯ СУММА ===
    total_el = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_el.text
    assert total_text == "Total: $58.29", f"Ожидали $58.29, а получили {total_text}"

    driver.quit()
