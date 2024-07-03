from django.urls import path
from . import views

# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.products, name='all_tea'),
    # path('order/', views.order, name='order'),

]