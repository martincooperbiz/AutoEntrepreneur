import unittest
from Auto-Entrepreneur.ai import AI

class TestAI(unittest.TestCase):
    def test_generate(self):
        ai = AI()
        response = ai.generate("Hello, world!")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
