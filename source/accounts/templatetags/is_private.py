from django import template

register = template.Library()


@register.filter
def is_private(file, user):
    return file.private_files.filter(user=user).count() > 0
