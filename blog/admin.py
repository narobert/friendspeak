from django.contrib import admin
from blog.models import Wpost, Ppost, Profile, Wcomment, Pcomment, Wlike, Wdislike, Plike, Pdislike

admin.site.register(Wpost)
admin.site.register(Ppost)
admin.site.register(Profile)
admin.site.register(Wcomment)
admin.site.register(Pcomment)
admin.site.register(Wlike)
admin.site.register(Wdislike)
admin.site.register(Plike)
admin.site.register(Pdislike)
