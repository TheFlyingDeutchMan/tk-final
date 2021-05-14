from behave import *
from pprint import pprint
import os

from assessmentv3 import venue_capacity_validation

@given(u'the venue {venue}')
def step_impl(context,venue):
    context.venue = venue

@given(u'an booking size of {booking_size}')
def step_impl(context,booking_size):
    context.booking_size = booking_size

@then(u'venue_capacity_valition should return {expected}')
def step_impl(context, expected):
    if expected == 'Pass':
        assert (venue_capacity_validation(context.venue,context.booking_size) is True)
    else:
        assert (venue_capacity_validation(context.venue,context.booking_size) is False)
