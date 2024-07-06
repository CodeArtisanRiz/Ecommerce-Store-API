from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('<int:product_id>/', RecommendationView.as_view(), name='recommendation-view'),
]
