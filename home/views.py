from django.shortcuts import render
from .models import book_table
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home/index.html')


def handle_form(request):
    res = ""
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        datetime = request.POST.get("datetime")
        num_people = request.POST.get("selection")
        srequest = request.POST.get("message")
        data = book_table(name=name,email=email,date_time=datetime,num_people_field=num_people,special_req=srequest)
        data.save()
        res = "Table Booked"
    return render(request,{'res':res})
        
