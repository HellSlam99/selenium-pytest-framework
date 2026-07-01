import pytest


@pytest.mark.parametrize(

    "username,password",

    [

        ("standard_user", "wrong"),

        ("wrong", "secret_sauce"),

        ("wrong", "wrong")

    ]

)

def test_invalid_login(

        app,

        username,

        password

):

    login = app["login"]

    login.login(

        username,

        password

    )

    expected = "Epic sadface: Username and password do not match any user in this service"

    assert login.get_error_message() == expected