from django.contrib import admin
from .models import book_table
from .form import bookingForm

admin.site.register(book_table)
