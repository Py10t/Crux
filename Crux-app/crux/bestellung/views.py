from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Order
from stock.models import Nummernkreise
from .tables import OrderTable
from django.shortcuts import redirect
from .forms import OrderForm, CollectiveOrderForm


from django.views.generic.edit import CreateView, UpdateView, DeleteView


# gets table data and displays it
def index(request):
    """index view is a table showing all orders"""
    table_single = OrderTable(Order.objects.filter(order_status="Bestellung", collection=False))
    table_collection = OrderTable(Order.objects.filter(order_status="Bestellung", collection=True))
    RequestConfig(request).configure(table_single)
    context = {
        'table_single': table_single,
        'table_collection': table_collection,
    }
    return render(request, 'bestellung/index.html', context)

# gets record_id from the table to update corresponding object/obj.order_status and take it to the next lvl
# afterwards page refresh
def update_order(request, record_id):
    """update orders order_status überführt von einer Stufe zur nächsten"""
    obj = Order.objects.get(pk=record_id)
    obj.order_status = 'Auftrag'
    obj.save()
    print('item updated: ' + str(record_id))
    response = redirect('/bestellung/')
    return response

def create_order(request):
    """create a single new order"""
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        order = form.save(commit=False)

        # this gets the order_number from DB, increment and save
        # db_number = Nummernkreise.objects.values_list('order_number', flat=True).get(pk=1)

        obj = Nummernkreise.objects.get(pk=1)
        obj.order_number +=1
        order.order_number_int = obj.order_number

        order.save()
        obj.save()

        response = redirect('/bestellung/')
        return response

    context = {
        "form": form,
    }
    return render(request, 'bestellung/order_form.html', context)

def create_collective_order(request):
    """create multiple orders that should refer to the same name"""
    form = CollectiveOrderForm(request.POST or None, request.FILES or None)
    print(CollectiveOrderForm)
    print(type(CollectiveOrderForm))
    if form.is_valid():
        print("FORM STARTS")
        for key in request.POST:
            print(key + "=")
            value = request.POST[key]
            print(value)
        print("FORM ENDS")


        order = form.save(commit=False)
        # print(order)

        # this gets the order_number from DB, increment and save
        # db_number = Nummernkreise.objects.values_list('order_number', flat=True).get(pk=1)

        # obj = Nummernkreise.objects.get(pk=1)
        # obj.order_number +=1
        # order.order_number_int = obj.order_number

        # order.save()
        # obj.save()

        response = redirect('/bestellung/new_collective_order/')
        return response

    context = {
        "form": form,
        # "form2": form2
    }
    return render(request, 'bestellung/collective_order_form.html', context)

# def create_album(request):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         form = OrderForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             album = form.save(commit=False)
#             album.user = request.user
#             album.album_logo = request.FILES['album_logo']
#             file_type = album.album_logo.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'Image file must be PNG, JPG, or JPEG',
#                 }
#                 return render(request, 'music/create_album.html', context)
#             album.save()
#             return render(request, 'music/detail.html', {'album': album})
#         context = {
#             "form": form,
#         }
#         return render(request, 'music/create_album.html', context)