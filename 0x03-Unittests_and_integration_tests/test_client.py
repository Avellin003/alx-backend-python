#!/usr/bin/env python3
"""Tests for the client module."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repositories."""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/test_org/repos"
            )
            # Test that the list of repositories is what we expect.
            client = GithubOrgClient("test_org")
            # The result should be a list of the names of the repositories.
            result = client.public_repos()
            # The expected result is a list of the names of the repositories.
            expected = ["repo1", "repo2"]
            # The result should be equal to the expected result.
            self.assertEqual(result, expected)
            # The mock should have been called once.
            mock_public_repos_url.assert_called_once()
            # The mock should have been called once.
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": {"key": "my_license"}}, "other_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct value."""
        client = GithubOrgClient("test_org")
        # The result should be equal to the expected value.
        result = client.has_license(repo, license_key)
        # The result should be equal to the expected value.
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
