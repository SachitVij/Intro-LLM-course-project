import unittest

def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        while len(series) < n:
            next_fib = series[-1] + series[-2]
            series.append(next_fib)
        return series

class TestFibonacciSeries(unittest.TestCase):

    def test_n_less_than_or_equal_to_zero(self):
        self.assertEqual(fibonacci_series(0), [])
        self.assertEqual(fibonacci_series(-5), [])

    def test_n_equals_one(self):
        self.assertEqual(fibonacci_series(1), [0])

    def test_n_equals_two(self):
        self.assertEqual(fibonacci_series(2), [0, 1])

    def test_n_greater_than_two(self):
        self.assertEqual(fibonacci_series(3), [0, 1, 1])
        self.assertEqual(fibonacci_series(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_series(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_large_n(self):
        # A moderately large number to ensure the loop works correctly
        # without being excessively long for a unit test.
        # The 15th Fibonacci number is 377
        expected_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        self.assertEqual(fibonacci_series(15), expected_series)

if __name__ == '__main__':
    unittest.main()
