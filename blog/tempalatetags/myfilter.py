from django import template
register = template.Library()


@register.filter
def mouth_upper(key):
    return ['一', '二', '三', ' 四', '五', '六', '七', '八', '九', '十', '十一', '十二']
