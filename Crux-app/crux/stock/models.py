from django.db import models
from django.urls import reverse

# Create your models here.

class Material(models.Model):
    """"Materialdaten"""
    name = models.CharField(("Material"), max_length=50)
    chem_name = models.CharField(("Tech. Name"),max_length=50)
    company =  models.CharField(("Firma"), max_length=50)

    def __str__(self):
        return self.name
        """ + ' | ' + self.chem_name + ' | ' + self.company"""


class Article(models.Model):
    """Artikeldaten"""
    ext_number = models.CharField(("Ext. ID"), max_length=50)
    int_number = models.CharField(("Int. ID"), max_length=50)
    name = models.CharField(("Artikel"), max_length=50)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    weight = models.DecimalField(("Gewicht"), max_digits=8, decimal_places=3)
    # stock_amount = models.BigIntegerField(("Lagerbestand"), default=0)
    price_per_piece = models.DecimalField(("Preis in €"), max_digits=8, decimal_places=2)
    cavities = models.BigIntegerField("Kavitäten", default=1)

    def __str__(self):
        return self.name + ' | ' + str(self.material)


class Stock(models.Model):
    """Lagerbestand"""
    article = models.OneToOneField('stock.Article', on_delete=models.CASCADE)
    stock_amount = stock_amount = models.BigIntegerField(("Lagerbestand"), default=0)

    def __str__(self):
        return str(self.stock_amount)


class MouldingMachine(models.Model):
    """Maschinendaten"""
    name = models.CharField(("Maschine"), max_length=50)
    power = models.BigIntegerField(("Tonnen"), default=0)
    power_consumption = models.BigIntegerField(("Max. Stromverbrauch"), default=0)
    injection_unit_volume = models.BigIntegerField(("Volumen in cm³"), default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    """Kundendaten"""
    name = models.CharField(("Kunde"), max_length=50, default="noname")
    city = models.CharField(("Stadt"), max_length=50, default="nocity")
    street = models.CharField(("Straße"), max_length=50, default="nostreet")
    phone = models.CharField(("Telefon"), max_length=50, default="nophone")
    email = models.EmailField

    def __str__(self):
        return self.name


class Tooling(models.Model):
    """Werkzeugdaten"""
    name = models.CharField(("Wkz-Name"), max_length=50)
    related_articles = models.ManyToManyField(Article)
    related_engines = models.ManyToManyField(MouldingMachine)

    def __str__(self):
        return self.name


class Nummernkreise(models.Model):
    """Nummern für z.B. Rechnungen und andere interne Dokumente"""
    year = models.BigIntegerField(default=19)
    order_number = models.BigIntegerField(default=0)
    task_number = models.BigIntegerField(default=0)
    prod_number = models.BigIntegerField(default=0)
    delivery_number = models.BigIntegerField(default=0)
    invoice_number = models.BigIntegerField(default=0)

    def __str__(self):
        return 'Nummernkreis PK=' + str(self.pk)