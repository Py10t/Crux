from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Order
from .tables import OrderTable
from django.shortcuts import redirect
from .forms import OrderForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView


# gets table data and displays it
def index(request):

    table = OrderTable(Order.objects.filter(order_status="Bestellung"))
    RequestConfig(request).configure(table)
    return render(request, 'bestellung/index.html', {'table': table})

# gets record_id from the table to update corresponding object/obj.order_status and take it to the next lvl
# afterwards page refresh
def update_order(request, record_id):

    obj = Order.objects.get(pk=record_id)
    obj.order_status = 'Auftrag'
    obj.save()
    print('item updated: ' + str(record_id))
    response = redirect('/bestellung/')
    return response
    # table = OrderTable(Order.objects.filter(order_status="Bestellung"))
    # RequestConfig(request).configure(table)
    # return render(request, 'bestellung/index.html', {'table': table})

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

def create_order(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.save()
        response = redirect('/bestellung/')
        return response

    context = {
        "form": form,
    }
    return render(request, 'bestellung/order_form.html', context)