from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('accounts/profile/', views.profile_veiew, name = 'profile'),
    path('add_ride/', views.add_ride, name='add_ride'),
    path('locations_data/', views.loc_data, name='loc_data'),

]
