from django import forms
from .models import Hotel,Booking

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'location', 'image']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out',
            'billing_address', 'billing_city', 'billing_state',
            'billing_zip', 'billing_country']