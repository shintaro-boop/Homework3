import pytest
def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
@pytest.mark.smoke
def test_01() :
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

@pytest.mark.smoke
def test_02() :
    with pytest.raises(IndexError):
        all_division()

@pytest.mark.smoke
def test_03() :
    result = all_division(2,-2)
    assert result == -1

@pytest.mark.hihi
def test_04 ():
    result = all_division(1000000, 1000, 10)
    assert result == 100.0

@pytest.mark.hihi
def test_05 () :
    result = all_division(0.001, 0.01)
    assert  0.1 ==pytest.approx(result)
