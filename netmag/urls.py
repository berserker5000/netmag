from django.conf.urls import patterns, include, url
from blog.models import Category, Post
from django.contrib import auth

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.index'),
	url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
	url(r'^contacts','blog.views.contacts'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'blog/login.html'}),
	url(r'^accounts/profile/$', 'blog.views.profile'),
	url(r'^accounts/logout/', 'blog.views.logout_view'),
	url(r'^accounts/register/', 'blog.views.register'),
)
