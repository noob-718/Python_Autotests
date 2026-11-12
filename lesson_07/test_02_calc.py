import pytest
from selenium import webdriver
from slow_calculator import SlowCalculatorPage


@pytest.mark.parametrize("browser", ["chrome"])
def test_slow_calculator(browser):
    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)
    page.set_delay(45)
    page.click_number(7)
    page.click_operator("+")
    page.click_number(8)
    page.click_equals()
    result = page.get_result()
    assert result == "15", f"Ожидали '15', а получили '{result}'"
    driver.quit()
    