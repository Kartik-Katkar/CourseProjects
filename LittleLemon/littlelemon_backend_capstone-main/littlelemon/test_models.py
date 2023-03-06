from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.test import TestCase
from restaurant.models import Booking, Menu

# test models 
class BookingModelTest(TestCase):
    # create a new booking
    def setUp(self):
        Booking.objects.create(first_name="Test", reservation_date=timezone.now(), reservation_slot=10)

    # test if the booking is created
    def test_booking_content(self):
        booking = Booking.objects.get(id=1)
        expected_object_name = f'{booking.first_name}'
        self.assertEqual(expected_object_name, 'Test')

class MenuModelTest(TestCase):
    # create a new menu item
    def setUp(self):
        Menu.objects.create(name="Test", price=10, menu_item_description="Test")

    # test if the menu item is created
    def test_menu_content(self):
        menu = Menu.objects.get(id=1)
        expected_object_name = f'{menu.name}'
        self.assertEqual(expected_object_name, 'Test')