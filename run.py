import pytest

pytest.main(

    [

        "-v",

        "--html=main/src/reports/report.html",

        "--self-contained-html"

    ]

)