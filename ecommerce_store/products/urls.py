from django.urls import path
from . import views

# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.products, name='products'),
    # path('order/', views.order, name='order'),

]