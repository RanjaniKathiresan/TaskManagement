from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_task/', views.save_task, name='save_task')
    
]