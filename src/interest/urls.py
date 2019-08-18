from django.urls import path
from .views import InterestListView,UserInterestListView,InterestCreateView
from . import views

urlpatterns = [
    path('', InterestListView.as_view(), name='my-interest-list'),
    path('new/', InterestCreateView.as_view(), name='create-interest-list'),
]