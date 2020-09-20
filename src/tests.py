from src.element import UserRegistration, AddItemsToCart


class TestCaseOne:
    def test_user_login(self):
        UserRegistration().open_login_page()
        UserRegistration().login_or_create_user()


class TestCaseTwo:
    def test_item_purchase(self):
        AddItemsToCart().add_items_to_cart()
        AddItemsToCart().checkout_items()
        AddItemsToCart().check_order_history()
