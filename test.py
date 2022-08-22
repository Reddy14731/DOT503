import main
import unittest


class TestArithmetic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(main.add(1, 2), 3, msg='Equal')
    def test_sub(self):
        self.assertEqual(main.sub(2, 2), 0, msg='Equal')
    def test_sub(self):
        self.assertEqual(main.sub(4, 2), 2, msg='Equal')
    def test_sub(self):
        self.assertEqual(main.mul(4, 2), 8, msg='Equal')
    def test_div(self):
        self.assertEqual(main.mul(4, 2), 8, msg='Equal')


if __name__ == '__main__':
    unittest.main()
