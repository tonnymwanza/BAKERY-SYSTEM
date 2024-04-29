from django.test import TestCase

from . models import Products
from . models import Contact
# Create your tests here.

class ContactTestCase(TestCase):
    
    def setUp(self):
        self.contact = Contact.objects.create(
            name='kevin', email='kevin@gmail.com', subject='urgent', message='my message'
        )

    def test_contact(self):
        self.assertEqual(self.contact.name, 'kevin')
        self.assertEqual(self.contact.email, 'kevin@gmail.com')
        self.assertEqual(self.contact.subject, 'urgent')
        self.assertEqual(self.contact.message, 'my message')

class ProductTestCase(TestCase):

    def setUp(self):
        self.product = Products.objects.create(
            name='wheat', price=250, description='pure wheat flour'
        )

        def test_product(self):
            self.assertEqual(self.product.name,'wheat')
            self.assertEqual(self.product.price, 250)
            self.assertEqual(self.product.description, 'pure wheat flour')