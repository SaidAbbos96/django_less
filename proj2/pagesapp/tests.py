from django.test import TestCase


class SimpleTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get("/about/")
        print(response)
        self.assertEqual(response.status_code, 200)


