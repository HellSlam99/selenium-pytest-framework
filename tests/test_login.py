def test_valid_login(app):

    login = app["login"]

    inventory = app["inventory"]

    login.login(

        "standard_user",

        "secret_sauce"

    )

    assert login.is_login_successful()

    assert inventory.get_page_title() == "Products"