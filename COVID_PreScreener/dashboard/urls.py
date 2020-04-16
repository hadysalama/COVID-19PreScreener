from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name="about"),
    path('resources/', Resources.as_view(), name="resources"),
    path('actions/', Actions.as_view(), name="actions"),
]