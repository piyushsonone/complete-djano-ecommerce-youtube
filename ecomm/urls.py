from django.contrib import admin
from django.conf.urls import url, include  # Add 'include' import here
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.urls import *
from products.urls import *
from accounts.urls import *

urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^product/', include("products.urls")),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
