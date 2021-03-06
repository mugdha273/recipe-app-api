from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating an user with eamil"""
        
        email = 'testuser@gmail.com'
        password = 'demopass123'
        
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        email = "demoemail@GMAIL.com"
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email, password = password
        )
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
            
    def test_new_create_user(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)