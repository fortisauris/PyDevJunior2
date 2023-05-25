import unittest  # vanilla python
from unittest.mock import Mock
from session23 import give_me_five, get_status

mock = Mock()  # falosny objekt
mock.__str__ = Mock(return_value='BRYNDZAZDRAZELA')

class TestGiveMeFive(unittest.TestCase):

    def test_response(self):
        self.assertEqual(give_me_five(), 5)
        # assert give_me_five() == 5

    def test_status(self):
        self.assertTrue(get_status())

    def test_zeroDivision(self):
        with self.assertRaises(ZeroDivisionError):
            print(give_me_five()/0)


class TestMockObject(unittest.TestCase):

    def test_mockingstring(self):
        self.assertEqual(mock.__str__(), 'BRYNDZAZDRAZELA')


if __name__ == '__main__':
    unittest.main()

# TODO Prestavka do 19:55