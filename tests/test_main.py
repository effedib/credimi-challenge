from unittest import TestCase
from main import app


class TestMyApp(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        result = self.app.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_retrieve_docs(self):
        result = self.app.get('/<fiscal_code>')
        self.assertEqual(result.status, '200 OK')