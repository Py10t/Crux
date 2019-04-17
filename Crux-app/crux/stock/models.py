from django.db import models
from django.urls import reverse

# Create your models here.

class Material(models.Model):
    name = models.CharField(("Material"), max_length=250)
    chem_name = models.CharField(("Tech. Name"),max_length=250)
    company =  models.CharField(("Firma"), max_length=250)

    def __str__(self):
        return self.name
        """ + ' | ' + self.chem_name + ' | ' + self.company"""


class Article(models.Model):
    ext_number = models.CharField(("Ext. ID"), max_length=250)
    int_number = models.CharField(("Int. ID"), max_length=250)
    name = models.CharField(("Artikel"), max_length=250)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    weight = models.DecimalField(("Gewicht"), max_digits=8, decimal_places=3)
    stock_amount = models.BigIntegerField(("Lagerbestand"), )
    currently_produced = models.BigIntegerField(("In Produktion"), )
    price_per_piece = models.DecimalField(("Preis in €"), max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name + ' | ' + str(self.material)


class Customer(models.Model):
    name = models.CharField(("Material"), max_length=250)
    adress = models.CharField(("Material"), max_length=250)
    phone = models.CharField(("Material"), max_length=250)
    email = models.EmailField



# Nummern für z.B. Rechnungen und andere interne Dokumente
class Nummernkreise(models.Model):
    year = models.BigIntegerField(default=19)
    order_number = models.BigIntegerField(default=0)
    task_number = models.BigIntegerField(default=0)
    prod_number = models.BigIntegerField(default=0)
    delivery_number = models.BigIntegerField(default=0)
    invoice_number = models.BigIntegerField(default=0)

    def __str__(self):
        return 'Nummernkreis PK=' + str(self.pk)