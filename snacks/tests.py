from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snacks


class MovieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snacks = Snacks.objects.create(
            name="Goldfish", description="description test", purchase=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snacks), "Goldfish")

    def test_movie_content(self):
        self.assertEqual(f"{self.snacks.name}", "Goldfish")
        self.assertEqual(f"{self.snacks.purchase}", "tester")
        self.assertEqual(f"{self.snacks.description}", "description test")

    def test_movie_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Goldfish")
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_movie_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Owner: 'tester'")
        self.assertTemplateUsed(response, "snacks_detail.html")

    def test_movie_create_view(self):
        response = self.client.post(
            reverse("snacks_create"),
            {
                "name": "Raker",
                "description": "test",
                "owner": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("snacks_detail", args="2"))
        self.assertContains(response, "Details about Raker")
