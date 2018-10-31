from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', index, name='home'),
    path('chat/<str:room_name>/', room),
]