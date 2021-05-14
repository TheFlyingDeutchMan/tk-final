from assessmentv3 import name_validation
from behave import *

import os


@given('a name {name}')
def step_impl(context, name):
    context.name = name


@given(u'a name ')
def step_impl(context):
    context.name = ''


@then(u'validate_name should return {expected}')
def step_impl(context, expected):
    if expected == 'True':
        assert (name_validation(context.name) is True)
    else:
        assert (name_validation(context.name) is False)
