from django.template import Library;

register = Library()

@register.filter(name='times') 
def times(number):
    
    if isinstance(number, str):
        return None
    return range(number)

@register.filter(name='timesminus') 
def timesminus(number):
    if isinstance(number, str):
        return None
    return range(5-number)