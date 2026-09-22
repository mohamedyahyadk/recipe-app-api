"""
Test for user  model .
"""

from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
        """
          testing for creating user model .
        """
        def test_create_user_email_successful(self):
           email="mohamed@example.com"
           password="ali123"
           user=get_user_model().objects.create_user(
                 email=email,
                 password=password
           )
           self.assertEqual(user.email,email)
           self.assertTrue(user.check_password(password))
        def test_new_user_normalize(self):
            samples_of_emails=[
                 ['test1@GMAIL.com','test1@gmail.com'],
                 ['test2@GMAIL.com','test2@gmail.com'],
                 ['test3@GMAIL.com','test3@gmail.com'],
                 ['test4@GMAIL.com','test4@gmail.com'],
                 
            ]
            for email, expected in samples_of_emails:
                 user=get_user_model().objects.create_user(email,'test123')
                 self.assertEqual(user.email,expected)
        def test_new_user_without_emai_raises_error(self):
             """Test that creating a new user without email raises a ValueError ."""
             with self.assertRaises(ValueError):
                  get_user_model().objects.create_user('','ff123')
        def test_create_superuser(self):
             """ Test creating a super user ."""
             user=get_user_model().objects.create_superuser(
                  'test@example.com',
                  'sampl123'
             )
             self.assertTrue(user.is_superuser)
             self.assertTrue(user.is_staff)
             
                