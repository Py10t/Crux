from django.db import models
import datetime
from django.core.validators import int_list_validator

# Create your models here.
class Maschine(models.Model):
    maschine_name = models.CharField(("Maschine"), max_length=250, default="Maschine X")
    manufacturer = models.ForeignKey('stock.Customer', on_delete=models.CASCADE)
    # zeitplan = models.CharField(validators=[int_list_validator], max_length=100)
    time_per_week = models.BigIntegerField(("Laufzeit"), default=1440)


class Auftragsobjekt(models.Model):
    name = models.ForeignKey('stock.Article', on_delete=models.CASCADE)
    start_date = models.DateField(("Lieferdatum"), default=datetime.date.today)
    runtime = models.BigIntegerField(("Laufzeit"), default=1440)
    auftrags_kw = models.BigIntegerField(("Laufzeit"), default=1440)

    # date_of_start = self.entries[2].get()
    # day, month, year = date_of_start.split('.')
    # auftrag_kw = datetime.date(int(year), int(month), int(day)).isocalendar()[1]
    #
    # print(datetime.date(int(year), int(month), int(day)).weekday())
    #
    # startzeit = datetime.date(int(year), int(month), int(day)).weekday() * 4 + int(self.entries[3].get())
    #
    # schuss = int(self.entries[4].get()) / int(self.entries[5].get())
    # dauer = int(schuss * int(self.entries[6].get()) / 60 / 60 / 6)
    pass
