import pytest

@pytest.fixture(scope='session') # you can also use scope as "module"
def setting_up():
    print("These statements to set-up Initially")
    yield
    print("These statements to tear-down session")

def test_01(setting_up):
    print("This is from test 01")

def test_02(setting_up):
    print("This is from test 02")

def test_03(setting_up):
    print("This is from test 03")

