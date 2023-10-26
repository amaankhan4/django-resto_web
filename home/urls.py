from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path("home/", views.home_page,name="home-home"),
    path("about/",views.about_page,name="home-about"),
    path("booking/",views.booking_page,name="home-book-a-table"),
    path("contact/",views.contact_page,name="home-contact"),
    path("menu/",views.menu_page,name="home-menu"),
    path("service/",views.service_page,name="home-service"),
    path("team/",views.team_page,name="home-team")
]