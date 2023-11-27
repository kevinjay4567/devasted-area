from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('catastrofe', views.catastrofe_detector, name="detector")
]