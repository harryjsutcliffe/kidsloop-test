import unittest
import robot


class TestRobot(unittest.TestCase):
    robot = robot.Robot()

    def test_get_sum_of_digits_basic(self):
        self.assertEqual(self.robot.get_sum_of_digits(11), 2)
        self.assertEqual(self.robot.get_sum_of_digits(-11), 2)
        self.assertEqual(self.robot.get_sum_of_digits(999), 27)
        self.assertEqual(self.robot.get_sum_of_digits(-999), 27)
        self.assertEqual(self.robot.get_sum_of_digits(100000), 1)
        self.assertEqual(self.robot.get_sum_of_digits(-100000), 1)
        self.assertEqual(self.robot.get_sum_of_digits(0), 0)

    def test_check_point_safe_basic(self):
        self.assertEqual(self.robot.check_point_safe((59, 75)), False)
        self.assertEqual(self.robot.check_point_safe((-59, -75)), False)
        self.assertEqual(self.robot.check_point_safe((59, -75)), False)
        self.assertEqual(self.robot.check_point_safe((-59, 75)), False)

        self.assertEqual(self.robot.check_point_safe((-51, 7)), True)
        self.assertEqual(self.robot.check_point_safe((51, -7)), True)
        self.assertEqual(self.robot.check_point_safe((-51, -7)), True)
        self.assertEqual(self.robot.check_point_safe((51, 7)), True)

        self.assertEqual(self.robot.check_point_safe((0, 0)), True)

    def test_check_point_safe_invalid(self):
        self.assertRaises(ValueError, self.robot.check_point_safe, (1, 1, 1))
        self.assertRaises(ValueError, self.robot.check_point_safe, (1))

    def test_get_neighbors(self):
        self.assertEqual(self.robot.get_neighbors((0, 0)), [
                         (0, 1), (1, 0), (0, -1), (-1, 0)])
        self.assertEqual(self.robot.get_neighbors((999, 999)), [
                         (999, 1000), (1000, 999), (999, 998), (998, 999)])


if __name__ == '__main__':
    unittest.main()
