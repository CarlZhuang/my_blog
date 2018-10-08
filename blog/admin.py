# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # 设置只显示
    fields = ('title', 'desc', 'content', 'tag', 'user', 'category')
    # 显示描述
    list_display = ('title',)

    class Media:
        js = (
               '/static/js/editor/kindeditor/kindeditor-all-min.js',
               '/static/js/editor/kindeditor/lang/zh-CN.js',
               '/static/js/editor/kindeditor/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)



