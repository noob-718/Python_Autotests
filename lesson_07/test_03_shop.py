import pytest
from selenium import webdriver
from saucedemo import LoginPage, HomePage, CartPage, CheckoutPage


@pytest.mark.parametrize("browser", ["firefox"])
def test_saucedemo(browser):
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Шаг 1–2: авторизация
    login_page.login("standard_user", "secret_sauce")

    # Шаг 3–4: добавление товаров + корзина
    home_page.add_to_cart("add-to-cart-sauce-labs-backpack")
    home_page.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    home_page.add_to_cart("add-to-cart-sauce-labs-onesie")
    home_page.go_to_cart()

    # Шаг 5: checkout
    cart_page.go_to_checkout()

    # Шаг 6–7: данные + summary
    checkout_page.fill_form("Иван", "Петров", "123456")
    checkout_page.go_to_summary()

    # Шаг 8: проверка суммы
    total = checkout_page.get_total()
    assert total == "Total: $58.29", f"Ожидали Total: $58.29, а получили {total}"

    driver.quit()
    