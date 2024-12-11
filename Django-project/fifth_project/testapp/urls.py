from django.urls import path
from testapp import views

urlpatterns = [
    path('first/', views.first_view, name='first'),
    path('second/', views.second_view, name='second'),
    path('third/', views.third_view, name='third'),
    path('fourth/', views.fourth_view, name='fourth'),
    path('fifth/', views.fifth_view, name='fifth'),
]