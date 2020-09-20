from src.element import MakePurchase


class TestCaseTwo:
    def test_item_purchase(self):
        MakePurchase().add_items_to_cart()
        MakePurchase().checkout_items()
        MakePurchase().check_order_history()
