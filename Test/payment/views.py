from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item, Order
import stripe
from django.http import HttpRequest, JsonResponse
from django.db.models import Sum
# Create your views here.




class BuyView(APIView):
	def get(self, request, pk):
		order = Order.objects.get(pk = pk)
		items = order.item.all()
		total_price = items.aggregate(Sum('price'))
		order_name = f"Order #{pk}"
		stripe.api_key = 'sk_test_51LkUkGE0hznV006AvUNjVykKyx9HovhZb6rbnxEGcCat9xnvPJ5XIWx7bmMwbEchMh2lj5TsKRvYgR73pELC7h1H00oPJcSyzY'
		session = stripe.checkout.Session.create(
		    line_items=[{
		      'price_data': {
		        'currency': 'usd',
		        'product_data': {
		          'name': order_name,
		        },
		        'unit_amount':total_price['price__sum'],
		      },
		      'quantity': 1,
		    }],
		    mode='payment',
		    success_url='https://example.com/success',
		    cancel_url='https://example.com/cancel',
		  )
		session_id = session.id

		return JsonResponse({'sessionId': session['id']})

def Items(request,pk):
	order = Order.objects.get(pk = pk)
	context = {'id':order.id,'order':order.item.all()}
	return render(request, 'payment/index.html',context)
