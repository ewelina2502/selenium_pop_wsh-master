from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage


class CartSummaryPage(BasePage):
    product_description_selector = (By.CSS_SELECTOR, ".cart_description > .product-name  > a")
    total_product = (By.ID, 'total_product')
    total_shipping = (By.ID, 'total_shipping')

    def check_the_price_smaller_50(self):
        price_number = self.driver.find_element(*self.total_product).text
        assert float(price_number.strip('$')) < 50
        print("price is smaller than 50")

    def check_the_total_shipping_2(self):
        price_total_shipping = self.driver.find_element(*self.total_shipping).text
        assert float(price_total_shipping.strip('$')) == 2
        print("shipping price is equal 2 dollars")
