
from django.urls import path
from blog.views import index, archive, article
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    url(r'^archive/$', archive, name='archive'),
    url(r'^article/$', article, name='article'),

]
