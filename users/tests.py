from django.test import TestCase
from users.models import User

class UserModelTests(TestCase):
    def test_create_user_with_role(self):
        user = User.objects.create_user(username='johndoe', password='password123', role='staff')
        self.assertEqual(user.role, 'staff')
        self.assertTrue(user.check_password('password123'))
