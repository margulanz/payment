
from django.urls import path
from .views import BuyView, Items

urlpatterns = [
    path('buy/<int:pk>/',BuyView.as_view(),name = 'buy'),
    path('item/<int:pk>/',Items,name = 'item'),
]