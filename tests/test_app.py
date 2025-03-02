import unittest
from app import hello_devops

class TestApp(unittest.TestCase):
    def test_hello_devops(self):
        self.assertEqual(hello_devops(), "Hello DevOps")

if __name__ == '__main__':
    unittest.main()
