
import pytest

def test_add1():
    assert 2+3 == 5

def test_add2():
    assert 4+5 == 9

@pytest.mark.parametrize("a , b , result" ,[
    (2,3,5),
    (4,5,9),
    (10,2,12)

])

def test_add(a , b , result):
    assert a+b == result


#single parameter
@pytest.mark.parametrize("number", [1,2,3,4,5])
def test_even(number):
    assert number %2 == 0


@pytest.mark.parametrize("payload" , [
    {"name": "Jhon", "age":25},
    {"name": "Alice", "age":17}
])
def test_crate_user(payload):
    assert payload["age"] > 18