from django.conf.urls import patterns, include, url

urlpatterns = patterns(

    'blog.views',

    (r'getCommentsW$', 'getCommentsW'),
    (r'getCommentsP$', 'getCommentsP'),
    (r'getLikeW$', 'getLikeW'),
    (r'getLikesW$', 'getLikesW'),
    (r'getDislikeW$', 'getDislikeW'),
    (r'getLikeP$', 'getLikeP'),
    (r'getLikesP$', 'getLikesP'),
    (r'getDislikeP$', 'getDislikeP'),

)
