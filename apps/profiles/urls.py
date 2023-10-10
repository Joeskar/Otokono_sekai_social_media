from django.urls import path

from .views import UserPublicView, UserPrivateView

urlpatterns = [
    path('profile/<int:pk>/', UserPrivateView.as_view()),
    path('profile/', UserPublicView.as_view({'get': 'list'})),
]
