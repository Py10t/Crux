from django.db import models

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