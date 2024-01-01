from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.

def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نیست',
            'icon': 'error',
            'confirm_button_text': 'باشه'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(order=current_order,
                                                                        product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_order_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_order_detail.save()
            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید اضافه شد ',
                'icon': 'success',
                'confirm_button_text': 'باشه'
            })
        else:
            return JsonResponse({
                'status': 'not found',
                'text': 'محصول مورد نظر یافت نشد',
                'icon': 'error',
                'confirm_button_text': 'باشه'

            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول مورد نظر به سبد خرید باید وارد حساب کاربری خود شوید',
            'icon': 'error',
            'confirm_button_text': 'باشه'
        })
