from django.urls import *
from .views import *
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('',index, name='index'),
    path('servcices',services, name='services'),
    path('photo',photo,name="photo"),
    path('activites',activites,name="activites"),
    path('contact',contact,name="contact"),
    # path('message',message,name='message')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)