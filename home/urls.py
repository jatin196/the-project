from django.urls import path
from .  import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('', views.index, name='index'),
]