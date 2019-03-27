from django.db import models
import datetime
from django.urls import reverse

# Create your models here.
class Order(models.Model):
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    company = models.CharField(("Firma"), max_length=250)
    amount = models.BigIntegerField(("Menge"))
    order_date = models.DateField(("Bestelldatum"), default=datetime.date.today)
    delivery_date = models.DateField(("Lieferdatum"), default=datetime.date.today)
    order_status = models.CharField(max_length=250, default="Bestellung")

    def get_absolute_url(self):
        return reverse('bestellung_index')

    def __str__(self):
        return self.article.name + ' | ' + str(self.amount) + ' | ' + str(self.company)