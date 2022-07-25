import pytest
from ..models import *
from django import urls
from django.contrib.auth import get_user_model
from django.test import Client


# function Run once per test
# class    Run once per class of tests
# module   Run once per module
# session  Run once per session

# ________________________________________ # To test models with ImageField

from io import BytesIO
from PIL import Image
from django.core.files.base import File

def create_test_image():
    file_obj = BytesIO()
    image = Image.new("RGBA", size=(50, 50), color=(256, 0, 0))
    image.save(file_obj, 'png')
    file_obj.seek(0)
    return File(file_obj, name="test_image.png")
# ________________________________________

@pytest.mark.django_db
@pytest.mark.parametrize('url', [('/category/'), ('/termin/'), ('/post/')])
def test_views_get(client, url):
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_creation(client):
    response = client.post('/category/', {'name': "Test", "image": create_test_image()})
    print(response.content)
    assert response.status_code == 302

@pytest.mark.django_db
def test_post_creation(client):
    category = Category.objects.create(name="Test", image="Test")
    response = client.post('/post/', {'title': "Test", "category": category.id})
    assert response.status_code == 302
    assert Post.objects.first().posttype == "post"

@pytest.mark.django_db
def test_termin_creation(client):
    category = Category.objects.create(name="Test", image="Test")
    response = client.post('/post/', {'title': "Test", "abbreviation": "Test", "longed": "Test", "text": "Test Text"})
    assert response.status_code == 302


# This fixture will run once though it will be used multiple times
@pytest.fixture(scope="module")
def user_data():
    return 1

# This fixture will run when every time it is called
@pytest.fixture
def user_data2():
    return 1
