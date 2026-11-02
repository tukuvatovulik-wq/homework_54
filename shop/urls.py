from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_view, name="products"),
    path("products", views.products_view),
    path("products/<int:product_id>/", views.product_detail_view, name="product_detail"),
    path("products/<int:product_id>/edit", views.product_edit_view, name="product_edit"),
    path("categories", views.categories_view, name="categories"),
    path("categories/<int:category_id>/edit", views.category_edit_view, name="category_edit"),
    path("categories/<int:category_id>/delete", views.category_delete_view, name="category_delete"),
]
