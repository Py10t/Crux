from django.shortcuts import render
from django.template import loader
from stock.models import Article
from bestellung.models import Order
from maschinenplanung.models import Auftragsobjekt
import datetime
# Create your views here.


def index(request):
    """renders index view, needs args for rectangle sizes"""
    day_week_month = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'maschinenplanung/index.html', {'articles': Article.objects.all()})


def mp(request):
    """gathers data from db.objects and constructs useful objects for the mp"""
    order_obj=Order.objects.filter(order_status="Produktionsauftrag", collection=False)
    print(len(order_obj))

    # aktuelle KW
    dt = datetime.datetime.now()
    current_kw = dt.isocalendar()[1]
    current_week_string = "KW " + str(current_kw)
    print(current_week_string)

    # Umwandlung aller order_objs in Auftragsobjekte aus models.py
    for item in order_obj:
        # print("item :" + str(item))
        planung_obj = Auftragsobjekt()
        artikelname = item.article.name
        # print("artikelname :" + str(artikelname) + str(type(item.article.name)))
        lieferdatum = item.delivery_date
        # print("lieferdatum :" + str(lieferdatum))
        liefermenge = item.amount
        # print("liefermenge :" + str(liefermenge))

        # prod dauer = menge / kavitätenanzahl * zykluszeit * 1.1 (10% Aufschlag)

        kav_anzahl = 4  # hardcoded, should be variable
        zykluszeit = 30  # hardcoded, should be variable
        produktionsdauer = int(liefermenge / kav_anzahl * zykluszeit * 1.1)
        # print("produktionsdauer :" + str(produktionsdauer))
        verpackungszeit = int(produktionsdauer/10)  # in Sekunden / 10 random Wert
        # print("verpackungszeit :" + str(verpackungszeit))
        summe = (produktionsdauer+30) / 3600  # +30 für ein-/ausbauen | Zeit in Stunden
        # print("summe :" + str(summe))

        # übergabe an die DB
        planung_obj.name = artikelname  # brauche ich was neues
        planung_obj.article = artikelname
        planung_obj.latest_finish = lieferdatum
        planung_obj.runtime = int(summe / 10080 * 100)
        # print("runtime :" + str(planung_obj.runtime))
        # saving object
        planung_obj.save()

    # all planung_objs into lists->amount related to the number of machines
    mp_objects=Auftragsobjekt.objects.all()  # should be filtered by machine :-)
    # sorted by ascending latest finish
    unsorted_mp_objects = mp_objects.all()
    sorted_mp_objects = sorted(unsorted_mp_objects, key=lambda t: t.latest_finish)
    print(sorted_mp_objects)

    # get current time and convert to number representing a starting time
    x = datetime.datetime.now()
    day = (int(x.strftime("%w"))-1) * 24 * 60  # -1 cause "0" = sunday; O_o who does that
    hour = int(x.strftime("%H")) * 60
    minute = int(x.strftime("%M"))
    print("day: " + str(day) + "/hour: " + str(hour) + "/minute: " + str(minute))
    # print(sorted_mp_objects[0].name)
    # print(sorted_mp_objects[0].runtime)
    starting_time = int((day + hour + minute + 30) / 10080 * 100)  # to get % numbers

    # creating starting time
    for item in sorted_mp_objects:
        item.starting_time = starting_time
        starting_time = starting_time + item.runtime
        # item.save()
        print(str(item.name) + "/starting time: " + str(item.starting_time) + "/runtime: " + str(item.runtime))

    mp_array = []

    for item in sorted_mp_objects:
        starting_time_2 = item.latest_finish - + datetime.timedelta(hours=item.runtime)
        print(starting_time_2)
        finishing_time = item.latest_finish
        print(finishing_time)
        mp_array.append(['Maschine 1', starting_time_2, finishing_time])
        pass

    print(mp_array)
    context = {
        'da_real_array': mp_array,
        'weekdays': ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag'],
        'machines': [1, 2, 3, 4, 5],  # len(all_machines) instead of hardcoded
        'ordered_list': sorted_mp_objects,
        'time': 15,
    }

    Auftragsobjekt.objects.all().delete()

    return render(request, 'maschinenplanung/index_test.html', context)