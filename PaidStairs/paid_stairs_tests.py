import unittest

from paid_stairs import PaidStairs

class TestPaidStairs(unittest.TestCase):
    def setUp(self):
        self.paidStairsCalculator = PaidStairs()

    def test_base_case_returns_zero(self):
        self.assertEqual(self.paidStairsCalculator.calculate(0, 0, [0]), 0, 'Base case of 0 num stairs did not return 0.')

    def test_negative_step_count_returns_zero(self):
        self.assertEqual(self.paidStairsCalculator.calculate(0, -1, [0]), 0, 'Negative step size did not return 0.')

    def test_varying_step_sizes_with_no_stairs(self):
        self.assertEqual(self.paidStairsCalculator.calculate(0, 1, [0]), 0, 'Step size of 1 with no stairs did not return 0.')
        self.assertEqual(self.paidStairsCalculator.calculate(0, 2, [0]), 0, 'Step size of 2 with no stairs did not return 0.')
    
    def test_varying_step_sizes_with_varying_stair_sizes(self):
        self.assertEqual(self.paidStairsCalculator.calculate(1, 1, [0, 1]), 1, 'Step size of 1 with stair size 1 did not return 1.')
        self.assertEqual(self.paidStairsCalculator.calculate(1, 2, [0, 1]), 1, 'Step size of 2 with stair size of 1 did not return 1.')
        self.assertEqual(self.paidStairsCalculator.calculate(2, 1, [0, 1, 2]), 3, 'Step size of 1 with stair size 2 did not return 3.')
        self.assertEqual(self.paidStairsCalculator.calculate(2, 2, [0, 1, 2]), 2, 'Step size of 2 with stair size of 1 did not return 1.')

    def test_varying_step_sizes_with_varying_stair_sizes_and_varying_prices(self):
        self.assertEqual(self.paidStairsCalculator.calculate(2, 1, [0, 2, 1]), 3, 'Step size of 1 with stair size 2 did not return 3.')
        self.assertEqual(self.paidStairsCalculator.calculate(3, 2, [0, 2, 1, 3]), 4, 'Step size of 2 with stair size of 1 did not return 1.')


if __name__ == '__main__':
    unittest.main()