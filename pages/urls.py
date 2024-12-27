from django.urls import path
from .views import HomePageView, AboutPageVeiw


urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("about/", AboutPageVeiw.as_view(), name="about_page")
]