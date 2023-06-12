import random
from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from iq_eq_app.models import TestUser


class TestIQEQ(APITestCase):
    def test_initalize_user(self):
        url = reverse("api/create_user")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("login", response.data)

    def test_save_iq(self):
        user = TestUser.objects.create(login="test_user")
        url = reverse("api/fill_iq")
        data = {"login": user.login, "iq": random.randint(0, 50)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["login"], user.login)

    def test_save_eq(self):
        user = TestUser.objects.create(login="test_user")
        url = reverse("api/fill_eq")
        data = {"login": user.login, "eq": "аабда"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["login"], user.login)

    def test_view_user(self):
        user = TestUser.objects.create(login="test_user")
        url = reverse("api/get_test_res")
        data = {"login": user.login}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["login"], user.login)

    def test_view_user_not_found(self):
        url = reverse("api/get_test_res")
        data = {"login": "nonexistent_user"}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# Create your tests here.
