import unittest
from unittest import result
import slur_count as slur


class TestSlur(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slur.slur_count(
            'Oh goodness slur1 slur2 what to do slur3 slur4'), 4)


if __name__ == '__main__':
    unittest.main()
