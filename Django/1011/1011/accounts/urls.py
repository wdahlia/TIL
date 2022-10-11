from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.main, name="main"),
    path('signup/', views.signup, name="signup"),
    path('index/', views.index, name="index"),
    path('<int:user_pk>/', views.detail, name="detail"),
]