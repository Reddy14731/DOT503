import main
import unittest


class TestArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(main.add(1, 2), 4, msg='Equal')


if __name__ == '__main__':
    unittest.main()
