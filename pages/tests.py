from django.test import TestCase


class PageTests(TestCase):
    def test_home_page(self):
        response = self.client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertIn('Lorum Online Shop'.encode(), response.content)

    def test_feedback_page(self):
        response = self.client.get('/feedback/')

        self.assertEqual(200, response.status_code)
        self.assertIn('leave your feedback about our company'.encode(), response.content)

    def test_thanks_for_feedback_page(self):
        response = self.client.get('/thanks-for-your-feedback/')

        self.assertEqual(200, response.status_code)
        self.assertIn('Thanks for your feedback'.encode(), response.content)
