from django import forms
from .models import Professional, Client, Appointment


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class ProfessionalSearchForm(forms.Form):
    q = forms.CharField(label='Buscar por nombre o email', required=False)
    profession = forms.ChoiceField(choices=[('', 'Todas')] + Professional.PROFESSION_CHOICES, required=False)
