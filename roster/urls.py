from django.conf.urls import url, include
from .views import roster

urlpatterns = [
    url(r'^roster/', roster, name="roster"),
]