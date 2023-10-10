from django.urls import path

from .views import UserOpenView

urlpatterns = [
    path('profile/', UserOpenView.as_view({'get': 'list'}))
]
