from . import views
from django.urls import path

app_name = 'runtest'

urlpatterns = [
    path('', views.index, name='index'),
]
