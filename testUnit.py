import unittest
from fastapi.testclient import TestClient
from fastapi import status
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()
