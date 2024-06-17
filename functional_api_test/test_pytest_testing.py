from pytest import mark


@mark.pytestTest
def test_pytest_method():
    print("Running Using Pytest")
    print("Hello Using Pytest")
    assert 1 == 2, "Not Matched"
