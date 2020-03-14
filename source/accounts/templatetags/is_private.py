from django import template

register = template.Library()


@register.filter
def is_private(file, user):
    return file.private_users.filter(user=user)
