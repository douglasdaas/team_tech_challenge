import unittest

from classes import DataCapture


class TestDataCapture(unittest.TestCase):
    def test_validate_bool(self):
        """Test that validate that boolean is not a valid input"""
        capture_bool = DataCapture()
        with self.assertRaises(ValueError, msg='It should return ValueError'):
            capture_bool.add(True)
        with self.assertRaises(ValueError, msg='It should return ValueError'):
            capture_bool.add(False)

    def test_validate_float(self):
        """Test that validate that float is not a valid input"""
        capture_float = DataCapture()
        with self.assertRaises(ValueError, msg='It should return ValueError'):
            capture_float.add(1.1)

    def test_validate_range(self):
        """Test that validate that the range of the input is between 0 an 999 inclusive"""
        capture_range = DataCapture()
        with self.assertRaises(ValueError, msg='It should return ValueError'):
            capture_range.add(-1)
        with self.assertRaises(ValueError, msg='It should return ValueError'):
            capture_range.add(1000)
        capture_range.add(500)
        self.assertEqual(capture_range.number_counter_dict, {500: 1})

    def test_validate_string(self):
        """Test that validate that integer in string format is a valid input"""
        capture_string = DataCapture()
        capture_string.add('2')
        self.assertEqual(capture_string.number_counter_dict, {2: 1})

    def test_validate_int(self):
        """Test that validate that integer is a valid input"""
        capture_int = DataCapture()
        capture_int.add(2)
        self.assertEqual(capture_int.number_counter_dict, {2: 1})

    def test_validate_stats(self):
        """Test that validate that, generated stats are correct"""
        capture_stats = DataCapture()
        capture_stats.add(3)
        capture_stats.add(9)
        capture_stats.add(3)
        capture_stats.add(4)
        capture_stats.add(6)
        self.assertEqual(capture_stats.number_counter_dict, {3: 2, 9: 1, 4: 1, 6: 1})
        stats = capture_stats.build_stats()
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.less(11), 5)
        self.assertEqual(stats.less(5), 3)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.between(6, 3), 4)
        self.assertEqual(stats.greater(4), 2)
        self.assertEqual(stats.greater(7), 1)
        self.assertEqual(stats.greater(2), 5)


if __name__ == '__main__':
    unittest.main()
