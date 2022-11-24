from django.urls import path
from .views import RideView, RideDetailView


urlpatterns = [
    path('', RideView.as_view(), name='all_rides'),
    path('<int:pk>/', RideDetailView.as_view(), name="ride"),
]