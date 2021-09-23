from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('contact/success', views.success, name="success"),
]