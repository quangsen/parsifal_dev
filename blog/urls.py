from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.entries, name='entries'),
    path('<slug>', views.entry, name='entry'),
]
