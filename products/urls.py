from django.urls import path

from products.views import TypeView, ProductListView

urlpatterns = [
    path('/categories/<int:category_id>/types', TypeView.as_view()),
    path('/categories', ProductListView.as_view()),
]
