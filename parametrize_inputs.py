import pytest

def squares(num):
    result=num*num
    return result

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5,25),
                            (6,36),
                             (100,10000)
                         ])
def test_squares(test_input,expected_output):
    result=squares(test_input)
    assert result == expected_output


