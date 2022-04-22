import unittest
from tasks import *


class MyTestCase(unittest.TestCase):
    def test_task108(self):
        with self.assertRaises(AssertionError):
            task_108("87hvg")
        with self.assertRaises(AssertionError):
            task_108(-9)
        with self.assertRaises(AssertionError):
            task_108(7.9)
        self.assertEqual(task_108(2), 2)
        self.assertEqual(task_108(1), 1)
        self.assertEqual(task_108(9), 4)
        self.assertEqual(task_108(8), 4)

    def test_task331a(self):
        with self.assertRaises(AssertionError):
            task_331a("87hvg")
        with self.assertRaises(AssertionError):
            task_331a(-9)
        with self.assertRaises(AssertionError):
            task_331a(7.9)
        self.assertEqual(task_331a(1), [])
        self.assertEqual(task_331a(21), [(1, 2, 4)])
        self.assertEqual(task_331a(67), [(3, 3, 7)])

    def test_task331b(self):
        with self.assertRaises(AssertionError):
            task_331b("87hvg")
        with self.assertRaises(AssertionError):
            task_331b(-9)
        with self.assertRaises(AssertionError):
            task_331b(7.9)
        self.assertEqual(task_331b(1), [])
        self.assertEqual(task_331b(21), [(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)])
        self.assertTrue((3, 3, 7) in task_331b(67))
        self.assertNotEqual(task_331b(1097), [(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)])
        self.assertTrue((13, 28, 12) in task_331b(1097))
        self.assertTrue((32, 3, 8) in task_331b(1097))
