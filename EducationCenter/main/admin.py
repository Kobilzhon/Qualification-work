from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


class ZayavkaAdmin(admin.ModelAdmin):
    list_display = ('message', 'phone_num', 'user')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(CourseCategory)
admin.site.register(Courses)
admin.site.register(MasterClass)
admin.site.register(Zayavka, ZayavkaAdmin)
admin.site.register(News)
admin.site.register(NewsComment)
# Register your models here.
