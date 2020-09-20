from selenium import webdriver
import src.page as page
from webdriver_manager.chrome import ChromeDriverManager


class AddItemsToCart:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('http://localhost')

    def add_items_to_cart(self):
        page.MainPage(self.driver).add_item_to_cart()

    def checkout_items(self):
        page.FillOrderCheckoutInfo(self.driver).checkout_purchase()

    def check_order_history(self):
        page.CheckPurchaseStatus(self.driver).check_order_history_status()


test2 = AddItemsToCart()
test2.add_items_to_cart()
test2.checkout_items()
test2.check_order_history()
