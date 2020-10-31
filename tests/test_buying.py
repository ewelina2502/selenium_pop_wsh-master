from pages.home import HomePage
from pages.products import ProductsPage
from pages.cart_summary import CartSummaryPage


def test_buy_different_products(driver):
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)
    cart_summary_page = CartSummaryPage(driver)

    home_page.search_product("Chiffon")
    products_page.add_element_to_cart()
    products_page.proceed_to_checkout()
    home_page.search_product("Blouse")
    products_page.add_element_to_cart()
    products_page.proceed_to_checkout()

    cart_summary_page.check_the_price_smaller_50()
    cart_summary_page.check_the_total_shipping_2()
