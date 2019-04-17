from django.db import models
import datetime
from django.urls import reverse
from stock.models import Nummernkreise

# Create your models here.
class Order(models.Model):
    collection = models.BooleanField(("Sammelbestellung"), default=False)
    collection_name = models.CharField(("Bestellungsname"), max_length=250, default="Single")
    order_number_int = models.BigIntegerField(("Bestellnummer intern"), default=0)
    order_number_ext = models.BigIntegerField(("Bestellnummer extern"), default=0)
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    company = models.CharField(("Kunde"), max_length=250)
    amount = models.BigIntegerField(("Menge"), default=0)
    order_date = models.DateField(("Bestelldatum"), default=datetime.date.today)
    delivery_date = models.DateField(("Lieferdatum"), default=datetime.date.today)
    order_status = models.CharField(max_length=250, default="Bestellung")

    def get_absolute_url(self):
        return reverse('bestellung_index')

    def __str__(self):
        return self.article.name + ' | ' + str(self.amount) + ' | ' + str(self.company)


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
#         return self.article.name + ' | ' + str(self.amount) + ' | ' + str(self.company)