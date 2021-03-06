from django import template
from django.contrib.auth.models import Group
from web.users.auth import auth_test
register = template.Library()
from web.users.statics import *


@register.filter(name='has_group')
def has_group(user, group_name):
    return auth_test(user, group_name)


@register.filter(name='is_user_type')
def is_user_type(user, user_type):
    return auth_test(user, user_type)


@register.filter(name='is_beheerder')
def is_beheerder(user):
    return auth_test(user, BEHEERDER)


@register.filter(name='is_begeleider')
def is_begeleider(user):
    return auth_test(user, BEGELEIDER)


