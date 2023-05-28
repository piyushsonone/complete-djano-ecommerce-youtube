from django.conf.urls import url
from products.views import get_product

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', get_product, name='get_product'),
]
