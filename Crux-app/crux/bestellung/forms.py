from django import forms
from stock.models import Nummernkreise

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_number_ext', 'article', 'company', 'amount', 'order_date', 'delivery_date']


class CollectiveOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['order_number_ext', 'collection_name', 'company', 'order_date']

class CollectiveOrderForm2(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['article', 'amount', 'order_date']