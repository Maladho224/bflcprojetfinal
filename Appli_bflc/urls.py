
from django.contrib import admin
from django.urls import path,include
from app_bflc import url


urlpatterns = [
    path('adminbflc/', admin.site.urls),
    path('',include('app_bflc.url')),
]
