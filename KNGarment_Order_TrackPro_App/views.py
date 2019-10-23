#External Imports
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.utils import timezone

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
#import json
#from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
#from bootstrap_modal_forms.generic import (BSModalCreateView,BSModalUpdateView,BSModalReadView,BSModalDeleteView)

#Project Imports
from KNGarment_Order_TrackPro_App.models import Client,Vendor,Orders,Process,Fabric_Order,Stiching,Washing,Finishing,Dispatch
#from payment.forms import GroupdescriptionForm, GroupdescriptionForm_UpdateForm, Client_UpdateForm, Vendor_UpdateForm,AddAirticket, AddVisacost,AddHotel,AddRestaurant,AddEntrances,AddSapsan,AddGuide,AddTransport,DateForm,ServiceForm_UpdateForm,CustomUserForm,AddAllservices

# Create your views here.

def add_new_order_form(request):
    return render(request,'KNGarment_Order_TrackPro_App/Add_orders.html')

def add_processes(request,pk):
    order_object = Orders.objects.get(pk=pk)
    data = {'orders':order_object}
    return render(request,'KNGarment_Order_TrackPro_App/add_processes.html',data)

def current_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Current.html')

def delivered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/delivered_orders.html')

def track_order_registered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Order_registered.html')

def track_order_details(request,pk):
    order_object = Orders.objects.get(pk=pk)
    data = {'orders':order_object}
    return render(request,'KNGarment_Order_TrackPro_App/Order_Details_2.html',data)

def track_order_fabric_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/fabric_order.html')

def track_order_stiching_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/stiching.html')

def track_order_washing_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Washing.html')

def track_order_finishing_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Finishing.html')

def track_order_dispatched_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/dispatch.html')

def payment_pending(request):
    return render(request,'KNGarment_Order_TrackPro_App/pending_order.html')

def payment_paid(request):
    return render(request,'KNGarment_Order_TrackPro_App/paid_order.html')

def reports_job_worker_balancereport(request):
    return render(request,'KNGarment_Order_TrackPro_App/job_worker_bal_report.html')

def reports_stockreport(request):
    return render(request,'KNGarment_Order_TrackPro_App/stock_report.html')

def track_order_production_details(request):
    return render(request,'KNGarment_Order_TrackPro_App/Production.html')

def report_error(request):
    return render(request,'KNGarment_Order_TrackPro_App/report_error.html')

def forget_password(request):
    return render(request,'KNGarment_Order_TrackPro_App/forget_password.html')

def user_login(request):
    return render(request,'KNGarment_Order_TrackPro_App/login_form.html')

def register(request):
    return render(request,'KNGarment_Order_TrackPro_App/register_form.html')

# Logout
def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:user_login'))

def add_new_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        order_order_number = request.POST['order_order_number']
        order_order_type = request.POST['order_order_type']
        order_order_brands = request.POST['order_order_brands']
        order_order_style_number = request.POST['order_order_style_number']
        order_order_fit = request.POST['order_order_fit']
        order_order_quantity = request.POST['order_order_quantity']
        order_order_date = request.POST['order_order_date']
        order_delivery_date = request.POST['order_delivery_date']
        order_order_category = request.POST['order_order_category']
        order_order_remark = request.POST['order_order_remark']
        Orders.objects.create(order_order_number = order_order_number,
                                        order_order_type = order_order_type,
                                        order_order_brands = order_order_brands,
                                        order_order_style_number = order_order_style_number,
                                        order_order_fit = order_order_fit,
                                        order_order_quantity = order_order_quantity,
                                        order_order_date = order_order_date,
                                        order_delivery_date = order_delivery_date,
                                        order_order_category = order_order_category,
                                        order_order_remark = order_order_remark,
                                        order_client_id = Client.objects.latest('pk'))
        orders_latest_object = Orders.objects.latest('order_order_date_of_entry') 

    return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:add_processes',kwargs={'pk': orders_latest_object.pk}))

def add_new_fabric_order_form_submit(request):
    if request.method == "POST":
        # Get all data relating to that order.
        fabric_order_sort_number = request.POST['fabric_order_sort_number']
        process_vendor_name = request.POST['process_vendor_name']
        process_received_quantity = request.POST['process_received_quantity']
        process_delivery_date = request.POST['process_delivery_date']
        Fabric_Order.objects.create(fabric_order_sort_number = fabric_order_sort_number,
                                        process_vendor_name = process_vendor_name,
                                        process_received_quantity = process_received_quantity,
                                        process_delivery_date = process_delivery_date,
                                        process_vendor_id=Vendor.objects.latest('pk'),
                                        process_order_id=Orders.objects.latest('pk'))
        Order_object = Orders.objects.latest('order_order_date_of_entry')
        
        return HttpResponseRedirect(reverse('KNGarment_Order_TrackPro_App:track_order_details',kwargs={'pk': Order_object.pk}))







