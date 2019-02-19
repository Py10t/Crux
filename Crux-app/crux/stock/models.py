from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.CharField(max_length=250)
    chem_name = models.CharField(max_length=250)
    company =  models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' | ' + self.chem_name + ' | ' + self.company


class Article(models.Model):
    ext_number = models.CharField(max_length=250)
    int_number = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=8, decimal_places=3)
    stock_amount = models.BigIntegerField()
    currently_produced = models.BigIntegerField()
    price_per_piece = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name + ' | ' + str(self.material) + ' | ' + str(self.stock_amount)