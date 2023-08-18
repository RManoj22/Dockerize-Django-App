"""
`from django.test import TestCase` is importing the `TestCase` class from the `django.test` module.
 This class is used for writing test cases in Django.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import MyTable


class MyTableModelTestCase(TestCase):
    """
    The MyTableModelTestCase class is a test case for testing
    the functionality of a custom table model.
    """

    def setUp(self):
        """
        The setUp function creates a test user and a test table
        entry with various fields.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.mytable = MyTable.objects.create(
            user=self.user,
            contact_number='+1234567890',
            client_name='Test Client',
            vendor_name='Test Vendor',
            vendor_company='Test Company',
            rate=100.0,
            currency='USD',
            contract_type='Remote',
            status='On Board',
            comments='Test comments'
        )

    def test_mytable_fields(self):
        """
        The function tests the fields of a table
        called "mytable" for specific values.
        """
        self.assertEqual(self.mytable.user, self.user)
        self.assertEqual(self.mytable.contact_number, '+1234567890')
        self.assertEqual(self.mytable.client_name, 'Test Client')
        data = self.mytable
        self.assertTrue(isinstance(data, MyTable))

    def test_mytable_str_method(self):
        """
        The function tests the __str__ method of
        the MyTable class by asserting that the string
        representation of the object is equal to
        the vendor_name attribute.
        """
        self.assertEqual(str(self.mytable), self.mytable.vendor_name)
