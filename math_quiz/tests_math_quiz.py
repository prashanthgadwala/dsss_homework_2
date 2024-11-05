import unittest
from math_quiz import generate_random_number, generate_random_operator, create_math_problem

class TestMathQuiz(unittest.TestCase):
    """
    Unit tests for the Math Quiz functions.
    """

    def test_generate_random_number(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random number {rand_num} out of range [{min_val}, {max_val}]")

    def test_generate_random_operator(self):
        """
        Test if the function returns one of the expected operators.
        """
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = generate_random_operator()
            self.assertIn(operator, operators, f"Operator {operator} not in {operators}")

    def test_create_math_problem(self):
        """
        Test the creation of math problems and their solutions.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (5.5, 2.2, '+', '5.5 + 2.2', 7.7),
            (5.5, 2.2, '-', '5.5 - 2.2', 3.3),
            (5.5, 2.2, '*', '5.5 * 2.2', 12.1)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem string {problem} does not match expected {expected_problem}")
            self.assertAlmostEqual(answer, expected_answer, places=1, msg=f"Answer {answer} does not match expected {expected_answer}")

if __name__ == "__main__":
    unittest.main()