from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest.views.home', name='home'),
    # url(r'^$', 'nes.views.home', name='home'),
    # url(r'^$', 'nes.views.search', name='home'),
    url(r'^$', 'nes.views.text_test', name='home'),
    url(r'^contact/?$', 'nes.views.contact',),
    url(r'^games/?', 'nes.views.search', name='game'),
    url(r'^random/?', 'nes.views.random_game', name='random'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*', 'nes.views.e404'),
)
