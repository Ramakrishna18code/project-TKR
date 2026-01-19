from django import template

register = template.Library()

@register.filter
def format_number(value):
    """Format number with commas for thousands"""
    try:
        num = int(value)
        return "{:,}".format(num)
    except (ValueError, TypeError):
        return value
