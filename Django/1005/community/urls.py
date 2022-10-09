from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]