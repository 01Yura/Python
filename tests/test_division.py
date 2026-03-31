from etc.division import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (1, 2, 0.5),
                                                   (30, -3, -10)])
def test_division_with_valid_arguments(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("a,b,expected_exception", [(10, 0, ZeroDivisionError),
                                                    (10, "string", TypeError)])
def test_division_with_error(a, b, expected_exception):
    with pytest.raises(expected_exception):
        division(a, b)
