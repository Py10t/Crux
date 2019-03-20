from django.db import models
import datetime

# Create your models here.
class Order(models.Model):
    article = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    company = models.CharField(max_length=250)
    amount = models.BigIntegerField()
    order_date = models.DateField(("Bestelldatum"), default=datetime.date.today)
    delivery_date = models.DateField(("Lieferdatum"), default=datetime.date.today)

    def __str__(self):
        return self.article.name + ' | ' + str(self.amount) + ' | ' + str(self.company)