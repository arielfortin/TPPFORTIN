from django import forms
from .models import Professional, Client, Appointment


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['first_name', 'last_name', 'profession', 'phone', 'email']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'email']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['professional', 'client', 'date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ProfessionalSearchForm(forms.Form):
    q = forms.CharField(required=False, label='Buscar profesional', max_length=100)
    profession = forms.ChoiceField(required=False, choices=[('', '---')] + Professional.PROFESSION_CHOICES)
