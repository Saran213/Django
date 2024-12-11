from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.portal, name='home'),
    path('movies/', views.movies, name ='movies'),
    path('sports/', views.sports, name ='sports'),
    path('politics/', views.politics, name ='politics'),
]
