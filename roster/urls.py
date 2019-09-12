from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', all_roster, name="roster"),
    url(r'^(?P<pk>\d+)/$', SingleWrestler.as_view(), name='single_wrestler')
]