import pytest
from ..models import *
from django import urls
from django.contrib.auth import get_user_model


# function Run once per test
# class    Run once per class of tests
# module   Run once per module
# session  Run once per session


# This fixture will run once though it will be used multiple times
@pytest.fixture(scope="module")
def user_data():
    return 1

# This fixture will run when every time it is called
@pytest.fixture
def user_data2():
    return 1


# @pytest.mark.parametrize('param', [('Termin-list'), ('Post-list')] )
# def test_render_views(client, param):
#     temp_url = urls.reverse(param)
#     resp = client.get(temp_url)
#     assert resp.status_code == 200


# @pytest.mark.django_db
def test_user_signup(user_data):
    assert 1 == user_data
    # user_model = get_user_model()
    # assert user_model.objects.count() == 0
    # signup_url = urls.reverse('Termin-list')
    # resp = client.post(signup_url, user_data)
    # assert user_model.objects.count() == 1
    # assert resp.status_code == 302






# Столько дней пропало, сколько пропадет
# Нам все это мало, жизнь не все дает
#
#