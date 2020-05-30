from django.test import TestCase
from django.contrib.auth.models import User

data = User.objects.filter(email='gokulyc@gmail.com')
print(data)
# Create your tests here.
