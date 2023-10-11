from django.urls import path

from .views import FollowerListView, FollowerSubscribeOrUnsubscribeView

urlpatterns = [
    path('', FollowerListView.as_view()),
    path('<int:pk>/', FollowerSubscribeOrUnsubscribeView.as_view())
]
