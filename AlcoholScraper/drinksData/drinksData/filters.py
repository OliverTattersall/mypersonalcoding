from django.template.defaulttags import register

@register.filter(name="multiply")
def multiply(value, arg):
    return value*arg