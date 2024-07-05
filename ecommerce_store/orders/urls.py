from django.urls import path
from .views import CreateOrderAPIView, ViewOrderAPIView, OrderListView

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),
    path('<int:order_id>/', ViewOrderAPIView.as_view(), name='view-order'),
    path('all/', OrderListView.as_view(), name='orders-list'),
]