from django.shortcuts import render, redirect, get_object_or_404
from shopapp.models import Product
from .models import Cart
from .models import Cartitem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=cart_id(request))
        cart.save()
    try:
        cart_item=Cartitem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
           cart_item.quantity +=1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cartapp:cart_detail')


def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))




def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cartitem=Cartitem.objects.get(product=product,cart=cart)
    if cartitem.quantity > 1:
        cartitem.quantity -=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cartapp:cart_detail')


def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cartitem = Cartitem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('cartapp:cart_detail')