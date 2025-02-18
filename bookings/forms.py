from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tour', 'guests', 'date']  # Ensure these fields exist in the Booking model
