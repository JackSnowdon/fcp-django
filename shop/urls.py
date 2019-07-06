from django.conf.urls import url, include 
from .views import all_shirts

urlpatterns = [
    url(r'^$', all_shirts, name="shirts")
    ]