from behave import *
import os

from assessmentv3 import email_validation

@given(u'an email {email}')
def step_impl(context,email):
    context.email = email

@then(u'validate_email should return {expected}')
def step_impl(context,expected):
    if expected == 'True':
        assert (email_validation(context.email) is True)
    else:
        assert (email_validation(context.email) is False)
