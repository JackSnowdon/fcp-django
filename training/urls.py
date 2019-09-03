from django.conf.urls import url, include
from .views import training

urlpatterns = [
    url(r'^training/', training, name="training"),
]