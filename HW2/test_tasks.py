import unittest
from tasks import *


class MyTestCase(unittest.TestCase):
    def test_task88(self):
        number1 = 8
        number2 = 19
        number3 = 1109
        self.assertEqual(task_88(number1), 8)
        self.assertEqual(task_88(number2), 91)
        self.assertEqual(task_88(task_88(number2)), 19)
        self.assertEqual(task_88(number3), 9101)

    def test_task88g(self):
        number1 = 8
        number2 = 19
        number3 = 1109
        self.assertEqual(task_88g(number1), 181)
        self.assertEqual(task_88g(number2), 1191)
        self.assertEqual(task_88g(task_88g(number2)), 111911)
        self.assertEqual(task_88g(number3), 111091)

    def test_task332(self):
        number1 = 1
        number2 = 8
        number3 = 19
        number4 = 1109
        self.assertTrue(1 in task_332(number1))
        self.assertTrue(2 in task_332(number2))
        self.assertTrue(3 in task_332(number3))
        self.assertTrue(22 in task_332(number4))
        self.assertFalse(10 in task_332(number1))
        self.assertFalse(10 in task_332(number2))
        self.assertFalse(10 in task_332(number3))
        self.assertFalse(10 in task_332(number4))
        self.assertTupleEqual(task_332(number1), (0, 0, 0, 1))
        self.assertTupleEqual(task_332(number2), (0, 0, 2, 2))
        self.assertTupleEqual(task_332(number3), (0, 1, 3, 3))
        self.assertTupleEqual(task_332(number4), (0, 0, 22, 25))


if __name__ == '__main__':
    unittest.main()
