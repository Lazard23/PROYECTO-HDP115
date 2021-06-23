from django.urls import path
from core.homepage.views.homepage.views import *
from core.homepage.views.usuarios.views import *

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('homepage/',UsuarioCreateView.as_view(),name='homepage'),
]