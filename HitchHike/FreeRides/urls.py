from django.urls import path, re_path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('accounts/profile/', views.profile_view, name='profile'),
path('add_ride', views.add_ride, name='add_ride'),
path('yes', views.yes, name='nooo'),
re_path(r'^(?P<ride_id>\d+)/$', views.detailed),

]
