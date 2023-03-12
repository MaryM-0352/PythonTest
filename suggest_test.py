import unittest
import suggest


class TestSuggester(unittest.TestCase):
    def setUp(self):
        self.my_suggerter = suggest.Suggester(suggest.SUGGEST_FILE)

    def test_maxSize(self):
        print()
        self.assertEqual(10, len(self.my_suggerter.get("")))

    def test_empty(self):
        self.assertListEqual(
            list(),
            self.my_suggerter.get(""))

    def test_default(self):
        self.assertEqual(
            list(),
            self.my_suggerter.get(None)
        )


if __name__ == "__main__":
    unittest.main()
