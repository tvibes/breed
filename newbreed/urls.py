from django.conf.urls import url
from . import views

# App URLs are entered below
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^collections/$', views.collections, name='collections')
]

