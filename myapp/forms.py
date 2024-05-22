from django.forms import ModelForm
from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.SelectDateWidget)
    booking_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'step': 900}),
        input_formats=['%H:%M']
    )
    number_of_people = forms.IntegerField()

    class Meta:
        model = Customer
        fields = '__all__'