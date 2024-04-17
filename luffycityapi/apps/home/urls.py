from django.urls import path
from luffycityapi.apps.home import views
urlpatterns = [
    path("nav/header/", views.NavHeaderListAPIView.as_view()),
    path("nav/footer/", views.NavFooterListAPIView.as_view()),
]
