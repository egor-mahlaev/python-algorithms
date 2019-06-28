from algorithms.search import (
    binary_search_iterative,
    binary_search_recursive,
    linear_search
)

import unittest


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.array = [1, 2, 3, 4, 5]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.array, 0), -1)
        self.assertEqual(linear_search(self.array, 1), 0)
        self.assertEqual(linear_search(self.array, 2), 1)
        self.assertEqual(linear_search(self.array, 3), 2)
        self.assertEqual(linear_search(self.array, 4), 3)
        self.assertEqual(linear_search(self.array, 5), 4)
        self.assertEqual(linear_search(self.array, 6), -1)

    def test_binary_search_iterative(self):
        self.assertEqual(binary_search_iterative(self.array, 0), -1)
        self.assertEqual(binary_search_iterative(self.array, 1), 0)
        self.assertEqual(binary_search_iterative(self.array, 2), 1)
        self.assertEqual(binary_search_iterative(self.array, 3), 2)
        self.assertEqual(binary_search_iterative(self.array, 4), 3)
        self.assertEqual(binary_search_iterative(self.array, 5), 4)
        self.assertEqual(binary_search_iterative(self.array, 6), -1)

    def test_binary_search_recursive(self):
        limit = len(self.array) - 1 # initial value for "right" argument
        self.assertEqual(binary_search_recursive(self.array, 0, 0, limit), -1)
        self.assertEqual(binary_search_recursive(self.array, 1, 0, limit), 0)
        self.assertEqual(binary_search_recursive(self.array, 2, 0, limit), 1)
        self.assertEqual(binary_search_recursive(self.array, 3, 0, limit), 2)
        self.assertEqual(binary_search_recursive(self.array, 4, 0, limit), 3)
        self.assertEqual(binary_search_recursive(self.array, 5, 0, limit), 4)
        self.assertEqual(binary_search_recursive(self.array, 6, 0, limit), -1)
