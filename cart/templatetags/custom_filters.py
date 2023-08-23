from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg

# 0823 cartlist(cart.html)에서 subtotal과 Total을 위한 코드추가
@register.filter
def total_price(cart_items):
    subtotal = 0
    for cart_item in cart_items:
        subtotal += cart_item.total_price
    return subtotal