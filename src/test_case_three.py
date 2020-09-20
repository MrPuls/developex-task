from src.element import UserRegistration, CreateReturnRequest


class TestCaseThree:
    def test_return_purchase(self):
        UserRegistration().create_user()
        CreateReturnRequest().create_return_request_and_verify_status()
