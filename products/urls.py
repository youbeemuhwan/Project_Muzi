from django.urls import path

from products.views import ProductCategoryView, ProductListView

urlpatterns = [
    # http://127.0.0.1:8000/products/categories/1
    path('/categories/<int:category_id>', ProductCategoryView.as_view()),

    # http://127.0.0.1:8000/products/categories/1/list
    path('/categories/<int:type_id>/list', ProductListView.as_view())
]
