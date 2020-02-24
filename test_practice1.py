

import pytest

#@pytest.fixture() # for pytest.fixyure(), there is no yield statements, this fixture method is used only to execute before executing methods
@pytest.yield_fixture()
def setup_method():
    print("\n","This is from setup method, Before calling Method")
    # yield
    # print("\n","This is from setup method, After executing Method")

def test_method1(setup_method):
    print("This call is from test_method1")

@pytest.mark.skip(reason="Just to test skippped test")
def test_method2():
    print("This call is from test_method2")
    i=10
    assert i==20

# Command to execute the file and generate a html report : pytest -v -s --html=report.html test_practice1.py
# Plugin required is pytest-html
 # Command to get more info on skipped test: E:\PYTEST_test_programs>pytest -v -rxs test_practice1.py

