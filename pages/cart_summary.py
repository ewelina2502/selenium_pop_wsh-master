from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage


class CartSummaryPage(BasePage):
    product_description_selector = (By.CSS_SELECTOR, ".cart_description > .product-name  > a")
    total_product = (By.ID, 'total_product')
    total_shipping = (By.ID, 'total_shipping')

    def get_all_elements(self):
        products_elements = self.driver.find_elements(*self.product_description_selector)
        products_name = ""
        for product in products_elements:
            products_name += product.text
        return products_name

    def check_the_price_smaller_50(self):
        price_number = self.driver.find_elements(*self.total_product)
        price = "$50.00"
        price_1 = price.strip("$")
        for price in price_number:
            price_number += price.text
            return price_1

        if price_1 == "50.00":
            return True

    def check_the_total_shipping_2(self):
        price_total_shipping = self.driver.find_elements(*self.total_shipping)
        shipping_price = "$2.00"
        price_2 = shipping_price.strip("$")
        for shipping_price in price_total_shipping:
            price_total_shipping += shipping_price.text
            return price_2

        if price_2 == "2.00":
            return True
