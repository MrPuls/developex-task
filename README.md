# developex-task

Tests are using DTO (src/tests_dto.py) to transfer data into tests

Test Cases covered:

1. User registration

- Go to http://localhost page
- Register a new account using fake userdata (My Account -> Register). Not private connection fix
- Logout from account
- Login to the account and verify registration data


2. Buy products

- Go to http://localhost page
- Login as user from TC_1 or register new one
- Add to cart 2 random products from “Featured” suggestion 
- Proceed to cart page
- Proceed to checkout page
- Fill required fields and confirm order
- Verify order status is “Pending” (My Account -> Order History)

3. Make purchase return
- Go to http://localhost page
- Login as user from TC_1, TC_2 or register new one
- Proceed to Order History
- Open order details
- Chose "return" option of random item
- Fill return info
- Verify order status is "Awaiting Products"