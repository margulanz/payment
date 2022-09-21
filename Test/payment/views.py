from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Item
import stripe
from django.http import HttpRequest, JsonResponse
# Create your views here.




class BuyView(APIView):
	def get(self, request, pk):
		item = Item.objects.get(pk = pk)
		stripe.api_key = 'sk_test_51LkUkGE0hznV006AvUNjVykKyx9HovhZb6rbnxEGcCat9xnvPJ5XIWx7bmMwbEchMh2lj5TsKRvYgR73pELC7h1H00oPJcSyzY'
		session = stripe.checkout.Session.create(
		    line_items=[{
		      'price_data': {
		        'currency': 'usd',
		        'product_data': {
		          'name': item.name,
		        },
		        'unit_amount': item.price,
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
	item = Item.objects.get(pk = pk)
	context = {'id':item.id,'product_name':item.name,'description':item.description,'price':item.price}
	return render(request, 'payment/index.html',context)



