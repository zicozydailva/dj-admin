from django import forms

from .models import Reservation

# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments']
#         widgets = {
#             'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }
#         labels = {
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'guest_count': 'Number of Guests',
#             'reservation_time': 'Reservation Time',
#             'comments': 'Additional Comments',
#         }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
    