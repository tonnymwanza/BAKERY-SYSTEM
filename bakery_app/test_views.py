from django.test import TestCase
from django.urls import reverse
# create your tests here

class HomeViewTestCase(TestCase):

    def test_home_url(self):
        self.response = self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response, 'home.html')

class AboutViewTestCase(TestCase):

    def test_about_url(self):
        self.response = self.client.post(reverse('about'))
        self.assertTemplateUsed(self.response, 'about.html')

class ServiceViewTestCase(TestCase):

    def test_service_url(self):
        self.response = self.client.get(reverse('service'))
        self.assertTemplateUsed(self.response, 'service.html')

class ProductViewTestCase(TestCase):

    def test_product(self):
        self.response = self.client.get(reverse('product'))
        self.assertTemplateUsed(self.response, 'product.html')

class ContactViewTestCase(TestCase):

    def test_product(self):
        self.response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(self.response, 'contact.html')