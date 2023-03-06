from django.test import TestCase
from restaurant.views import home, about, book, reservations, menu, display_menu_item, bookings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_book_view(self):
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_reservations_view(self):
        response = self.client.get(reverse('reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')

    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_display_menu_item_view(self):
        response = self.client.get(reverse('menu_item', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_item.html')

    def test_bookings_view(self):
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html')