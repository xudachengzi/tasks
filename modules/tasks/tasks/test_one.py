import pytest

a=1
b=2


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.run_these_please
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)
    assert 1 in (1,2,3)
    assert a <  b
    assert 'fizz'  not in 'fizzbuzz'


