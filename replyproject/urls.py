from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'replyproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')), 
    url(r'^$', 'postreply.views.home', name='home'),
    url(r'^add/$', 'postreply.views.addpost', name="addpost"),
    url(r'^getdata/$', 'postreply.views.getdata', name="getdata"),
    url(r'^home/$', 'postreply.views.postform', name="homepage"),
    url(r'^reply/$', 'postreply.views.addreply', name="addreply"),


    

)
