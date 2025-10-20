from django.shortcuts import render, redirect, get_object_or_404
from .models import Professional
from .forms import ProfessionalForm, ClientForm, AppointmentForm, ProfessionalSearchForm


# Home
def home(request):
    return render(request, 'agenda/home.html')


# Lista profesionales + buscador
def professional_list(request):
    form = ProfessionalSearchForm(request.GET or None)
    qs = Professional.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        profession = form.cleaned_data.get('profession')
    #if q:
    #    qs = qs.filter(models.Q(first_name__icontains=q) | models.Q(last_name__icontains=q) | models.Q(email__icontains=q))
    if profession:
        qs = qs.filter(profession=profession)
        return render(request, 'agenda/professional_list.html', {'professionals': qs, 'form': form})


# Crear profesional
def professional_create(request):
    if request.method == 'POST':
        form = ProfessionalForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('agenda:professional_list')
    else:
        form = ProfessionalForm()
        return render(request, 'agenda/professional_form.html', {'form': form})


# Crear cliente
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
    if form.is_valid():
        client = form.save()
        return redirect('agenda:appointment_create')
    else:
        form = ClientForm()
        return render(request, 'agenda/client_form.html', {'form': form})


# Crear cita
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('agenda:professional_list')
        except Exception as e:
            form.add_error(None, 'No se pudo agendar (posible conflicto de horario).')
        else:
            form = AppointmentForm()
            return render(request, 'agenda/appointment_form.html', {'form': form})