from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('detail/<int:pk>/', views.detail, name="detail"),
]
