
from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
    path('', views.main, name='main'),
    path('todo/', views.todo, name='todo'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_pk>/', views.delete, name='delete'),
    path('update/<int:todo_pk>/', views.update, name='update'),
    path('check/<int:todo_pk>/', views.check, name='check'),
]