from django.test import TestCase
from ..views import add

class TestSample(TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)