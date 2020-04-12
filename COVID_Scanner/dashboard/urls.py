from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
<<<<<<< HEAD
    path('about/', views.about, name="about"),
=======
>>>>>>> f7e61110e25b35eeacf4d2715058d4db4e9e7b8f
]