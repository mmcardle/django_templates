from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
from django.conf.urls.static import static
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='home'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
	url(r"^su/", include("django_su.urls")),

	# Auth
	url(r"^auth/", include("django.contrib.auth.urls")),
)

if settings.DEBUG:
	urlpatterns += patterns("",
		url(r"", include("django.contrib.staticfiles.urls")),
	) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)