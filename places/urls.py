from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.place_list, name='place_list'),
    path('add/', views.add_place, name='add_place'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
]