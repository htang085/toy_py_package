import unittest
from toy_py_package import add_numbers  # Import the function you want to test

class TestToyPyPackage(unittest.TestCase):
    """Tests for `toy_py_package` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass  # You can leave this empty for now if you don’t need any setup

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass  # You can leave this empty for now if you don’t need any teardown

    def test_add_numbers(self):
        """Test the `add_numbers` function."""
        self.assertEqual(add_numbers(2, 3), 5)  # Check 2 + 3 = 5
        self.assertEqual(add_numbers(-1, 1), 0)  # Check -1 + 1 = 0
        self.assertEqual(add_numbers(0, 0), 0)  # Check 0 + 0 = 0
        self.assertEqual(add_numbers(100, 200), 300)  # Check 100 + 200 = 300
