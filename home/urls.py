from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path("home/", views.home_page,name="home-home"),
    path("home/",views.handle_form,name="handle_booking_data")
]