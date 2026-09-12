import unittest
from tool import normalize


class TraceTests(unittest.TestCase):
    def test_sorts_and_removes_volatile_fields(self):
        result = normalize([{"timestamp": "2", "kind": "tool", "name": "x", "token_count": 9}, {"timestamp": "1", "kind": "model"}])
        self.assertEqual(result[0]["kind"], "model")
        self.assertNotIn("token_count", result[1])


if __name__ == "__main__":
    unittest.main()
