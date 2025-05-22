from django.test import TestCase, Client

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_not_found_url(self):
        response = self.client.get('/a-url-that-does-not-exist')
        self.assertEquals(response.status_code, 404)
