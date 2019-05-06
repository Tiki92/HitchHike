from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('accounts/profile/', views.profile_view, name='profile'),
path('add_ride', views.add_ride, name='add_ride'),
path('yes', views.yes, name='nooo'),

]
