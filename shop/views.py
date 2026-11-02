from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm


def products_view(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "shop/products.html", {"products": products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})


def product_edit_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("product_detail", product_id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, "shop/product_edit.html", {"form": form, "product": product})


def categories_view(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "shop/categories.html", {"categories": categories})


def category_delete_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
    return redirect("categories")


def category_edit_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)

    return render(request, "shop/category_edit.html", {"form": form, "category": category})
