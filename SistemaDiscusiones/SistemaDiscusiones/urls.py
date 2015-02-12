try:
	from django.conf.urls import include, patterns, url
except ImportError:
	from django.conf.urls.defaults import include, patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),

    
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.users.urls', namespace='users')),

    #PYTHON SOCIAL AUTH
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),


    url(r'^admin/', include(admin.site.urls)),
)
