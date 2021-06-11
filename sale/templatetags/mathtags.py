from django import template
import math

register = template.Library()  #Djangoテンプレートタグライブラリ


@register.filter()
def divide(n1, n2):
    try:
        return n1 / n2
    except (ZeroDivisionError, TypeError):
        return None


@register.filter()
def floor_divide(n1, n2):
    try:
        return n1 // n2
    except (ZeroDivisionError, TypeError):
        return None


@register.filter()
def multiply(n1, n2):
    try:
        return n1 * n2
    except TypeError:
        return None

@register.filter(name="percentof")
def percentof(value, args):
    percent = format((value / args) * 100 , '.0f') 
    print(type(percent))
    return percent + "%"

