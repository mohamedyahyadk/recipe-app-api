"""
Test for user  model .
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email=email, password=password)


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
        def test_create_recipe(self):
          """Test creating a recipe is successful."""
          user=get_user_model().objects.create_user(
               'test@exmaple.com',
               'test123',
            )
          recipe =models.Recipe.objects.create(
                user=user,
                title='Sample recipe description .',
                time_minutes=5,
                price=Decimal('5.50'),
                description='Sample recipe description.',
            )
          self.assertEqual(str(recipe),recipe.title)
        def test_create_tag(self):
          """Test creating a tag is successful."""
          user=create_user()
          tag=models.Tag.objects.create(user=user,name='Tag1')
          self.assertEqual(str(tag),tag.name)     
        def test_create_ingredient(self):
          """Test creating an ingredient is successful."""
          user=create_user()
          ingredient=models.Ingredient.objects.create(user=user,name='Ingredient1')
          self.assertEqual(str(ingredient),ingredient.name)