import modules.fut as fut
import pytest

@pytest.mark.parametrize('test_input1, test_input2, expected_result',
                            [
                                (1,2,3),
                                (2,3,5),
                                (100, 400, 500),
                                (-1, -2, -3)
                            ])
def test_calc_total(test_input1, test_input2, expected_result):
    assert fut.calc_total(test_input1,test_input2) == expected_result

