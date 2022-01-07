from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_projects/', views.get_projects, name='get_projects'), 
    path('blogs/', views.blogs, name='blogs'), 
]
