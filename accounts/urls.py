from django.conf.urls import url, include
from .views import logout, login, registration, user_profile, single_order
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset)),
    url(r'^(?P<pk>\d+)/$', single_order, name='single_order')
]