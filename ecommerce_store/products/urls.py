from django.urls import path
from . import views
from .views import ProductListView

urlpatterns = [
    path('', views.products, name='products'),
    path('view/', ProductListView.as_view(), name='product_list'),

]
