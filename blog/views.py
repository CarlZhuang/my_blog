from django.shortcuts import render
from django.conf import settings
from blog import models
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

# Create your views here.


def globe_setting(request):

    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_DESC": settings.SITE_DESC,
    }


def index(request):
    # 分类数据
    category_list = models.Category.objects.all()
    # 最新文章数据
    article_list = models.Article.objects.all()
    pagetor = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = pagetor.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = pagetor.page(1)
    # 标签
    tag_list = models.Tag.objects.all()
    # 广告
    ad_list = models.Ad.objects.all()

    return render(request, "index.html", locals())
