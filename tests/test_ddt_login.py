from main.src.utils.csv_reader import CSVReader

import pytest


users = CSVReader.read(

    "main/src/data/users.csv"

)


@pytest.mark.parametrize(

    "user",

    users

)

def test_ddt_login(

        app,

        user

):

    login = app["login"]

    login.login(

        user["user"],

        user["password"]

    )

    if user["result"] == "pass":

        assert login.is_login_successful()

    else:

        assert "Epic sadface" in login.get_error_message()