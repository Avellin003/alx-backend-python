#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class-wide mocks"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == "https://api.github.com/orgs/test_org":
                return org_payload
            elif url == "https://api.github.com/orgs/test_org/repos":
                return repos_payload
            return None

        cls.mock_get.return_value = MagicMock(
            json=MagicMock(side_effect=get_json_side_effect)
        )

    @classmethod
    def tearDownClass(cls):
        """Stop class-wide mocks"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, apache2_repos)


if __name__ == "__main__":
    unittest.main()
