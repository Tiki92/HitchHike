from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
path('', views.index, name='index'),
path('accounts/profile/', views.profile_view, name='profile'),
url(r'^accounts/profile/(?P<pk>\d+)/$', views.profile_view, name='profile_pk'),
path('add_ride', views.add_ride, name='add_ride'),
re_path(r'^(?P<ride_id>\d+)/$', views.detailed),
path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
