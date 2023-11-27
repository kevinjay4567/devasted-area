from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_page, name='index'),
    path('info', views.mostrar_info, name="info"),
    path('guardar', views.guardar_info, name='guardar')
]