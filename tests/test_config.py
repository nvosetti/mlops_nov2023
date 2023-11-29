
def test_generic() :
    a = 30
    b = 40
    assert a != b

class NotInRange(Exception) :
    def __init__(self, message="value not in given range - by Oracle India") :
        self.message = message
        super().__init__(self.message)