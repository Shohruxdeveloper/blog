from django import template
from blog.models import Category

register = template.Library()


@register.simple_tag
def all_categories():
    return Category.objects.all()