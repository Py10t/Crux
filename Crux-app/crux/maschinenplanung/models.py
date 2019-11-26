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
    """ week divided into 7 x (60*24) = 10080 units for each minute"""
    name = models.CharField(("Auftragsobjekt"), max_length=250, default="Something_name")
    article = models.CharField(("Auftragsobjekt"), max_length=250, default="Something:article")
    latest_finish = models.DateTimeField(("Lieferdatum"), default=datetime.datetime.today)
    runtime = models.BigIntegerField(("Laufzeit"), default=1440)
    auftrags_kw = models.BigIntegerField(("Ziel KW"), default=1440)
    # in case the production already started you want a fixed time and not a calculated
    prod_started = models.BooleanField(("Already started"), default=False)
    starting_time = models.BigIntegerField(("Startzeit"), default=1440)
    fixed_starting_time = models.BigIntegerField(("fStartzeit"), default=1440)

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
    def __str__(self):
        return self.name + ' | ' + str(self.latest_finish)
