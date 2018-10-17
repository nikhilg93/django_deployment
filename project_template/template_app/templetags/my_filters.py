# Custom filters
from django import template

register = template.Library()

# Method 1
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
register.filter('cut',cut)

# Method 2 using decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
