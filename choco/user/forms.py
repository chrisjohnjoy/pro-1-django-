from django import forms
from .models import bookingform

class DateInput(forms.DateInput):
    input_type='date'

class booking(forms.ModelForm):
    class Meta:
        model=bookingform
        fields='__all__'
        widgets={
            'purchase_date':DateInput()
        }
        labels={
            'title':"Product name",
            'customer_naame':"Customer name",

        }