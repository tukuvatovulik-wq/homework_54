from django.test import TestCase
from django.urls import reverse
from .models import Category, Product


class ProductEditTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books", description="Books")
        self.product = Product.objects.create(
            name="Some Title",
            category=self.category,
            price="100.00",
            image="https://example.com/image.jpg",
            description="Old description",
        )

    def test_edit_page_has_existing_values(self):
        response = self.client.get(reverse("product_edit", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some Title")

    def test_product_is_updated_and_detail_is_opened(self):
        response = self.client.post(
            reverse("product_edit", args=[self.product.id]),
            {
                "name": "New Title",
                "price": "150.00",
                "image": "https://example.com/new.jpg",
                "category": self.category.id,
                "description": "New description",
            },
        )
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "New Title")
        self.assertRedirects(response, reverse("product_detail", args=[self.product.id]))


class CategoryTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Games", description="Game category")

    def test_categories_page(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Games")

    def test_category_edit(self):
        response = self.client.post(
            reverse("category_edit", args=[self.category.id]),
            {"name": "New games", "description": "Updated"},
        )
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "New games")
        self.assertRedirects(response, reverse("categories"))

    def test_category_delete(self):
        response = self.client.post(reverse("category_delete", args=[self.category.id]))
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())
        self.assertRedirects(response, reverse("categories"))
