from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_chart/', views.post_chart, name='post_chart'),
]
