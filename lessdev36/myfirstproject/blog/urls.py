from django.urls import path
from . import views

urlpatterns = [
    # path('about/', views.about, name='about-club'),
    # path('time/', views.current_datetime, name='blog-home'),
    # path('greet/<str:name>/', views.greet, name='greet'),
    # path('', views.get_example, name='greet'),
    path('', views.index),
    path('postuser/', views.postuser),
]
