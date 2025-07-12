import unittest
from unittest.mock import MagicMock

from codemaintainergenie.memory import Memory

class TestMemory(unittest.TestCase):
    def test_memory_can_be_instantiated_with_mock_repo(self):
        mock_repo = MagicMock()
        mock_repo.default_branch = "main"
        mock_repo.get_commits.return_value = []
        mock_repo.get_issues.return_value = []
        mem = Memory(mock_repo)
        self.assertIsInstance(mem, Memory)

if __name__ == "__main__":
    unittest.main()