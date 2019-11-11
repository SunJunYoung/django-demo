from django.urls import path
from . import views

app_name='list'
urlpatterns = [
    path('', views.indexView, name="index"),
]
