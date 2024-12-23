from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key)

@register.filter
def replace(value, args):
    if ',' not in args:
        return value  # Если аргументы некорректны, возвращаем исходное значение
    old, new = args.split(',', 1)
    return float(value.replace(old, new))