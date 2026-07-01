def test_checkout_success(app):

    login = app["login"]

    inventory = app["inventory"]

    cart = app["cart"]

    checkout = app["checkout"]

    success = app["success"]

    login.login(

        "standard_user",

        "secret_sauce"

    )

    inventory.add_item(

        "Sauce Labs Backpack"

    )

    inventory.add_item(

        "Sauce Labs Bike Light"

    )

    inventory.open_cart()

    cart.checkout()

    checkout.checkout(

        "John",

        "Smith",

        "380015"

    )

    assert success.get_success_message() == "Thank you for your order!"