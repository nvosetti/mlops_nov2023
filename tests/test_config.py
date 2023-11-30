import pytest


class NotInRange(Exception) :
    def __init__(self, message="value not in given range - by Oracle India") :
        self.message = message
        super().__init__(self.message)


def test_generic() :
    a = 30
    b = 40
    assert a != b

def test_generic1():
    a = 5
    with pytest.raises(NotInRange) :
        if a not in range(10, 20) :
            raise NotInRange
        
def test_generic2():
    a = 15
    if a not in range(10, 20) :
        raise NotInRange

