from django.urls import path, include
from .views import get_name

urlpatterns = [
    path('', get_name),
]
