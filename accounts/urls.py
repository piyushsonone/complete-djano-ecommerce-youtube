from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import login_page, register_page, activate_email

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login_page, name="login"),
    url(r'^accounts/register/$', register_page, name="register"),
    url(r'^accounts/activate/(?P<email_token>[-\w]+)/$', activate_email, name="activate_email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
