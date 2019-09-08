from datetime import datetime

from django import template
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import pluralize

register = template.Library()


@register.filter
def active_link(value, link):
    link_data = link.split(",")
    link_data = list(map(str.strip, link_data))

    if len(link_data) == 1:
        link = reverse(link_data[0])
    else:
        link = reverse(link_data[0], args=(link_data[1]))

    if value == link:
        return "active"


@register.filter
def short_date(value):
    now = timezone.now()
    delta = now - value
    if delta.days >= 365:
        years = delta.days // 365
        return f"{years} year{pluralize(years)} ago."
    elif delta.days >= 30:
        months = delta.days // 30
        return f"{months} month{pluralize(months)} ago."
    elif delta.days >= 7:
        weeks = delta.days // 7
        return f"{weeks} week{pluralize(weeks)} ago."
    elif delta.days > 0:
        return f"{delta.days} day{pluralize(delta.days)} ago."
    elif delta.seconds >= 3600:
        hours = delta.seconds // 3600
        return f"{hours} hour{pluralize(hours)} ago."
    elif delta.seconds >= 60:
        minutes = delta.seconds // 60
        return f"{minutes} minute{pluralize(minutes)} ago."
    else:
        return "Just Now"


@register.simple_tag()
def current_time(format_string):
    return datetime.now().strftime(format_string)


@register.simple_tag()
def sum(a, b, *args, **kwargs):
    sum = a + b
    for num in args:
        sum += num
    return sum


@register.filter()
def is_detail(value):
    value = value.split("/")
    link_data = list(map(str.strip, value))
    v = link_data[len(link_data) - 2]
    if v.isnumeric() is True:
        return "short"
