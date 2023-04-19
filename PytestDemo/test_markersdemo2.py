import pytest
import sys


@pytest.mark.skip
def test_login():
    print("Login done")


@pytest.mark.skipif(sys.version_info>(3, 11), reason="Python version not supported")
def test_add_products():
    print("product added")


@pytest.mark.xfail
def test_logout():
    print("logout done")
    assert False
    print("Logout Done")
