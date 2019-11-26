from django.db import models
import datetime
from django.urls import reverse
from stock.models import Nummernkreise, Customer, Article

# Create your models here.
DEFAULT_CUSTOMER_ID = 1
class Order(models.Model):
    collection = models.BooleanField(("Sammelbestellung"), default=False)
    collection_name = models.CharField(("Bestellungsname"), max_length=250, default="Single")
    order_number_int = models.BigIntegerField(("Bestellnummer intern"), default=0)
    order_number_ext = models.BigIntegerField(("Bestellnummer extern"), default=0)
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE, verbose_name='Artikel')
    customer = models.ForeignKey('stock.Customer', on_delete=models.CASCADE, default=DEFAULT_CUSTOMER_ID, verbose_name='Kunde')
    amount = models.BigIntegerField(("Menge"), default=0)
    order_date = models.DateTimeField(("Bestelldatum"), default=datetime.datetime.today)
    delivery_date = models.DateTimeField(("Lieferdatum"), default=datetime.datetime.today)
    # production_starting_time = models.TimeField(("Startzeit"), default=datetime.datetime)
    order_status = models.CharField(("Status"), max_length=250, default="Bestellung")
    stock_amount = models.BigIntegerField(("Lagermenge"), default=0)

    def get_absolute_url(self):
        return reverse('bestellung_index')

    def __str__(self):
        return self.article.name + ' | ' + str(self.order_status) + ' | ' + str(self.customer)


# class CollectiveOrder(models.Model):
#     collection_name = models.CharField(max_length=250, default="Bestellung")
#     article_ids = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
#     company = models.CharField(("Firma"), max_length=250)
#     amount = models.BigIntegerField(("Menge"))
#     order_date = models.DateField(("Bestelldatum"), default=datetime.date.today)
#     delivery_date = models.DateField(("Lieferdatum"), default=datetime.date.today)
#     order_status = models.CharField(max_length=250, default="Bestellung")
#
#     def get_absolute_url(self):
#         return reverse('bestellung_index')
#
#     def __str__(self):
#         return self.article.name + ' | ' + str(self.amount) + ' | ' + str(self.customer)