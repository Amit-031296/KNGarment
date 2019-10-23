#External Imports
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
#from django.contrib.auth import login, logout, authenticate
#from django.urls import reverse_lazy, reverse
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
#import json
#from django.contrib.auth.hashers import make_password
#from django.core.mail import send_mail
#from bootstrap_modal_forms.generic import (BSModalCreateView,BSModalUpdateView,BSModalReadView,BSModalDeleteView)

# Create your views here.

def add_new_order_form(request):
    return render(request,'KNGarment_Order_TrackPro_App/Add_orders.html')

def add_processes(request):
    return render(request,'KNGarment_Order_TrackPro_App/add_processes.html')

def current_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Current.html')

def delivered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/delivered_orders.html')

def track_order_registered_order(request):
    return render(request,'KNGarment_Order_TrackPro_App/Order_registered.html')

def track_order_details(request):
    return render(request,'KNGarment_Order_TrackPro_App/Order_Details_2.html')

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






