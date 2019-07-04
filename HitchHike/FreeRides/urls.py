from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
path('', homeView.as_view(), name='index'),
path('accounts/profile/', profile.as_view(), name='profile'),
url(r'^accounts/profile/(?P<pk>\d+)/$', profile.as_view(), name='profile_pk'),
path('add_ride', addRide.as_view(), name='add_ride'),
re_path(r'^(?P<ride_id>\d+)/$', detailed.as_view()),
path('accounts/profile/edit/', editProfile.as_view(), name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
