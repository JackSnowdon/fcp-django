from django.conf.urls import url, include 
from .views import all_shirts, ItemDetailView

urlpatterns = [
    url(r'^$', all_shirts, name="shirts"),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail')
    ]