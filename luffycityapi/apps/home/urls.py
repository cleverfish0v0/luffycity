from django.contrib import admin
from django.urls import path
from luffycityapi.apps.home import views

urlpatterns = [
    path('test/', views.HomeAPIView.as_view()),
]
