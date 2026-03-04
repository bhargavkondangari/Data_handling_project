import pytest

@pytest.mark.smoketest
def test_func1():
    assert True
#pyest -k "smoketest" "spefic string running"
#pytest -m smoketest

@pytest.mark.parametrize("a,b,c",[(2,4,5)])
def test_func2(a,b,c):
    assert a+b+c == 10
#cmd : pytest -k "parametrize"
#pytest -m smoketest

@pytest.mark.smoketest
def test_func3():
    assert False
