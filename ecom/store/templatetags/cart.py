from django import template

register = template.Library()
global total  
@register.filter(name='cart_check')
def cart_check(product,cart):
    keys = cart.keys()
    for id in keys:
        # keys are stored as strings
        if id == str(product.id):
            return True
    return False


@register.filter(name='cart_count')
def cart_count(product,cart):
    keys = list(cart.keys())
    for id in keys:
        if int(id) == (product.id):
            return int(cart.get(id))
    return 0

@register.filter(name='total_price_per_product')
def total_price_per_product(product,cart):

    return int(product.price) * cart_count(product,cart)


    

@register.filter(name='total_price')
def total_price(products,cart):
    total_price=0
    for p in products:
        total_price += total_price_per_product(p,cart)
    return total_price


@register.filter(name='total_items')
def total_price(products,cart):
    total_items=0
    for p in products:
        total_items += cart_count(p,cart)
    return total_items