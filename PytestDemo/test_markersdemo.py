import pytest


@pytest.mark.smoke
def test_login():
    print("Login done")


@pytest.mark.regression
def test_add_products():
    print("product added")


@pytest.mark.smoke
def test_logout():
    print("logout done")

