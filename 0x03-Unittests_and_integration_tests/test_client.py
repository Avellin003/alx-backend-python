#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, {"login": "mocked_org"})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
