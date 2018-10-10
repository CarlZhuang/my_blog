from django.shortcuts import render
from django.conf import settings
from blog.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.db.models import Count
# Create your views here.


def globe_setting(request):
    # 分类
    category_list = Category.objects.all()
    # 标签
    tag_list = Tag.objects.all()
    # 文章归档
    archive_list = Article.objects.distinct_date()
    # 广告
    ad_list = Ad.objects.all()
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]

    return locals()


# 分页
def get_page(request, article_list):
    pagetor = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = pagetor.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = pagetor.page(1)
    return article_list


def index(request):
    # 最新文章数据
    article_list = Article.objects.all()
    article_list = get_page(request, article_list)
    return render(request, "index.html", locals())


def archive(request):
    year = request.GET.get('year', None)
    mouth = request.GET.get('month', None)
    article_list = Article.objects.filter(date_publish__icontains=year+'-'+mouth)
    article_list = get_page(request, article_list)
    return render(request, 'archive.html', locals())


def article(request):
    article_id = request.GET.get('article', None)
    article_content = Article.objects.all().filter(id=article_id)
    return render(request, 'article.html', locals())
