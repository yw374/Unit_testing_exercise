import pytest

@pytest.mark.parametrize("input1, input2, input3, input4, input5, expected", [
(2, 3, 4, 6, 4, 8),
(0.5, 4, 1.5, 12, 2, 6),
])
def test_calculate_output(input1, input2, input3, input4, input5, expected):
    from Unit_testing import calculate_output
    answer = calculate_output(input1, input2, input3, input4, input5)
    assert answer == expected
