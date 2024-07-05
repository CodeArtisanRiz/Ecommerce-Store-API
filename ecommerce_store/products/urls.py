from django.urls import path
from . import views
from .views import ProductListView, AddProductView


urlpatterns = [
    path('', views.products, name='products'),
    path('view/', ProductListView.as_view(), name='product_list'),
    path('create/', AddProductView.as_view(), name='add_product'),
]
