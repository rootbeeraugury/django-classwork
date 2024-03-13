from django.urls import path
from . import views

urlpatterns = [
  path("", views.home.as_view(), name="home"),
  path("about/", views.about.as_view(), name="about"),
  path("portfolio/", views.portfolio.as_view(), name="portfolio"),
  path("cats/", views.cats.as_view(), name="cats"),
  path("printingpress/", views.printingpress.as_view(), name="printingpress"),
  path("aliens/", views.aliens.as_view(), name="aliens"),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
]
