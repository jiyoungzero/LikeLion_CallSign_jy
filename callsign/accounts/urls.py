from urllib.parse import urlparse
from django.urls import path, include
from .views import *

app_name = "accounts"
urlpatterns = [
    path('logout/', logout, name="logout"),
    path('mypage/', mypage, name="mypage"),
    path('newinfo/', newinfo, name= 'newinfo'),
    path('information/', information, name="information"),
]