import sample

def test_return_number():
    assert sample.FizzBuzz(1) == 1

def test_return_Fizz():
    assert sample.FizzBuzz(3) == 'Fizz'

def test_return_Buzz():
    assert sample.FizzBuzz(5) == 'Buzz'