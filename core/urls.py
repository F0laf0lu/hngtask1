from django.urls import path
from .import views

urlpatterns = [
    path('api/', views.get_user_info, name='get_user_info'),
]
