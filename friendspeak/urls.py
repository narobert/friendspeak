from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    # url(r'^bullpost/', include('bullpost.foo.urls')),
    url(r'^logout/', 'blog.views.logout', name='logout'),
    url(r'^login/', 'blog.views.login', name='login'),
    url(r'^afterlogin/', 'blog.views.afterlogin', name='afterlogin'),
    url(r'^register/', 'blog.views.register', name='register'),
    url(r'^myprofile/', 'blog.views.myprofile', name='myprofile'),
    url(r'^post/', 'blog.views.postwall', name='postwall'),
    url(r'^postto/(?P<username>[\w\-]+)/$', 'blog.views.postprofile', name='postprofile'),
    url(r'^posttome/', 'blog.views.postmyprofile', name='postmyprofile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', 'blog.views.profile', name='profile'),
    url(r'^view/(?P<id>[\w\-]+)/$', 'blog.views.click', name='click'),
    url(r'^commentwall/(?P<id>[\w\-]+)/$', 'blog.views.commentwall', name='commentwall'),
    url(r'^commentprofile/(?P<id>[\w\-]+)/$', 'blog.views.commentprofile', name='commentprofile'),
    url(r'^commentpost/(?P<id>[\w\-]+)/$', 'blog.views.commentpost', name='commentpost'),
    url(r'^likewall/(?P<id>[\w\-]+)/$', 'blog.views.likewall', name='likewall'),
    url(r'^dislikewall/(?P<id>[\w\-]+)/$', 'blog.views.dislikewall', name='dislikewall'),
    url(r'^likeprofile/(?P<id>[\w\-]+)/$', 'blog.views.likeprofile', name='likeprofile'),
    url(r'^dislikeprofile/(?P<id>[\w\-]+)/$', 'blog.views.dislikeprofile', name='dislikeprofile'),

    # Trying out ajax comments
    (r'^ajax/blog/', include('blog.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
