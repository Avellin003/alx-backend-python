#!/usr/bin/env python3
"""Tests for utils.py."""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""
    def test_memoize(self):
        """Test that the memoize decorator caches the result of a method."""
        class TestClass:
            """A class with a method and a memoized property."""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as mock_method:
            test = TestClass()
            # Call the method twice, but the method should only be called once.
            self.assertEqual(test.a_property(), 42)
            # The method should not be called again.
            self.assertEqual(test.a_property(), 42)
            # The method should only be called once.
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
