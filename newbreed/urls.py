from django.conf.urls import url
from . import views

# App URLs are entered below
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^artisan/add/$', views.ArtisanCreate.as_view(), name='add-artisan'),
    url(r'^(?P<slug>[\w-]+)/$', views.photo_detail, name='detail'),
]

