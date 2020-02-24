import math_calc
import sys
import pytest

@pytest.fixture
def start_statements():
    print("The function ")




def test_math_calc_add():
    total=math_calc.math_calc_add(4,5)
    assert total==9,"The sum is not correct"

def test_math_calc_mul():
    product=math_calc.math_calc_mul(4,5)
    assert product==20,"The product is not correct"

@pytest.mark.skipif(sys.version_info > (3,5), reason="Python version is greater than 3.5, so skipping now")
def test_dummy1():
    assert True

@pytest.mark.windows_testcases
def test_windows_case01():
    assert True

@pytest.mark.windows_testcases
def test_windows_case02():
    assert True

#pytest -k math -v test_math_calc.py (To run test cases which has name math in that)
#pytest -v -rxs test_math_calc.py (To get more info on skipped test case)
#pytest -m windows_testcases -v (To run test case based on custom markers, here: windows_testcases)
#pytest -m "not windows_testcases" -v test_math_calc.py (To run all test cases other than windows_testcases here)
