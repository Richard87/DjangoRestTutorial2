from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .views import user_snippet_post


class TestUserSnippets(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_long_enough_title_is_successful(self):
        factory = APIRequestFactory()
        url = reverse(user_snippet_post, kwargs={"pk": 1})

        request = factory.post(url, {'title': 'new super-long idea!!!', 'code': "<?php echo  'Hello world!'"})
        response = user_snippet_post(request, pk=1)
        response.render()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_too_short_title_fails(self):
        factory = APIRequestFactory()
        url = reverse(user_snippet_post, kwargs={"pk": 1})

        request = factory.post(url, {'title': 'new idea', 'code': "<?php echo  'Hello world!'"})
        response = user_snippet_post(request, pk=1)
        response.render()

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)


    def test_that_always_fails(self):
        self.assertTrue(False)