from algorithms.search import (
    binary_search_iterative as bsi,
    binary_search_recursive as bsr,
    linear_search
)

import unittest


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.size = 5 # test array size
        self.array = [i for i in range(self.size)] # test array

    def test_linear_search(self):
        for i in range(self.size):
            with self.subTest(i=i):
                self.assertEqual(linear_search(self.array, i), i)
        self.assertEqual(linear_search(self.array, -1), -1)
        self.assertEqual(linear_search(self.array, self.size), -1)
        
    def test_binary_search_iterative(self):
        for i in range(self.size):
            with self.subTest(i=i):
                self.assertEqual(bsi(self.array, i), i)
        self.assertEqual(bsi(self.array, -1), -1)
        self.assertEqual(bsi(self.array, self.size), -1)

    def test_binary_search_recursive(self):
        for i in range(self.size):
            with self.subTest(i=i):
                self.assertEqual(bsr(self.array, i, 0, self.size - 1), i)
        self.assertEqual(bsr(self.array, -1, 0, self.size - 1), -1)
        self.assertEqual(bsr(self.array, self.size, 0, self.size - 1), -1)
