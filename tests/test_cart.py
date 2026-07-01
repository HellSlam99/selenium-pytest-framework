def test_add_remove_cart(app):

    login = app["login"]

    inventory = app["inventory"]

    cart = app["cart"]

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

    inventory.add_item(

        "Sauce Labs Bolt T-Shirt"

    )

    inventory.add_item(

        "Sauce Labs Fleece Jacket"

    )

    assert inventory.get_cart_count() == 4

    inventory.open_cart()

    assert cart.get_cart_count() == 4

    cart.remove_item(

        "Sauce Labs Fleece Jacket"

    )

    assert cart.get_cart_count() == 3