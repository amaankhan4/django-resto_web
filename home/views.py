from django.shortcuts import render

def home_page(request):
    return render(request, 'home/index.html')

def about_page(request):
    return render(request,"home/about.html")

def contact_page(request):
    return render(request,"home/contact.html")

def menu_page(request):
    return render(request,"home/menu.html")

def booking_page(request):
    return render(request,"home/booking.html")

def service_page(request):
    return render(request,"home/service.html")

def team_page(request):
    return render(request,"home/team.html")


