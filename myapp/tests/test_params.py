from django.test import TestCase


class MenuItems(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dishes = 'pasta falafel cheesecake'.split()
        cls.urls = [f'/dishes/{dish}' for dish in cls.dishes]
        cls.elements = [
            # {'url': url, 'dish':dish} for url, dish in
            (url, dish) for url, dish in
            zip(cls.urls, cls.dishes)
        ]
        return super().setUpClass()

    def test_response_dishes_200_subtests(self):
        for url in self.urls:
            with self.subTest(url=url, msg=f'hellooo {url}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)

    def test_dishes_contains_dish_subtests(self):
        for url, dish in self.elements:
            with self.subTest(url=url, dish=dish, msg=f'hellooo {url, dish}'):
                self.response = self.client.get(url)
                self.assertEqual(self.response.status_code, 200)
                self.assertContains(self.response, dish)