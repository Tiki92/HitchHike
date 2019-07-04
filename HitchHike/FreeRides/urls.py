from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url
from .views import *

urlpatterns = [
path('', homeView.as_view(), name='index'),
path('accounts/profile/', login_required(profile.as_view()), name='profile'),
url(r'^accounts/profile/(?P<pk>\d+)/$', login_required(profile.as_view()), name='profile_pk'),
path('add_ride', login_required(addRide.as_view()), name='add_ride'),
re_path(r'^(?P<ride_id>\d+)/$', detailed.as_view()),
path('accounts/profile/edit/', editProfile.as_view(), name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
