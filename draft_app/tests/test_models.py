from django.test import TestCase

from ..models import *

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Test", image="something.jpg")

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), self.category.name)


class TerminModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name="Test", image="something.jpg")
        category2 = Category.objects.create(name="Test 2", image="something.jpg")
        # category = Category.objects.all()
        cls.termin = Termin.objects.create(title="Test", abbreviation="TST", longed="test" ,image="something.jpg", text="Text is test")

    def test_termin_str_representation(self):
        self.assertEqual(str(self.termin), self.termin.title)


