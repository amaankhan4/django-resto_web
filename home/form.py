from django import forms
from .models import book_table

class bookingForm(forms.ModelForm):
    class meta:
        model = book_table
        fields = ['name','email','date_time','num_people_field','special_req']