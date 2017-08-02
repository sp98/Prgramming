import unittest


class SomeTest(unittest.TestCase):
    def test_one_plus_two(self):
        assert 1+2==3

    def test_one_minus_two(self):
        assert not 1-2==1

    def test_assert_equal(self):
        self.assertEqual(1, 1, 'assert equals failed')

    def test_assert_greater(self):
        self.assertGreater(3, 1, 'assert greater failed')

    def test_assert_less(self):
        self.assertLess(1, 3, 'assert less failed')

    def test_assert_in(self):
        self.assertIn(5, [1, 2, 3, 5], 'assert In failed')
        
if __name__ == '__main__':
    unittest.main()