from django.shortcuts import render, get_object_or_404, redirect
from .models import Professional
from .forms import ProfessionalForm, ClientForm, AppointmentForm, ProfessionalSearchForm
from django.db.models import Q
from django.http import HttpResponse
from django.forms import *
from django.contrib import messages

def index(request):
    return render(request, 'agenda/home.html')

def home(request):
    return render(request, 'agenda/home.html')

#def home(request):
#    return HttpResponse("<h1>¡Funciona la raíz2!</h1>")

def professional_list(request):
    form = ProfessionalSearchForm(request.GET or None)
    qs = Professional.objects.all()
    if form.is_valid():
        q = form.cleaned_data.get('q')
        profession = form.cleaned_data.get('profession')
        if q:
            qs = qs.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q))
        if profession:
            qs = qs.filter(profession=profession)
    return render(request, 'agenda/professional_list.html', {'professionals': qs, 'form': form})


def professional_create(request):
    if request.method == 'POST':
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = ProfessionalForm()
    return render(request, 'agenda/professional_form.html', {'form': form})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:appointment_create')
    else:
        form = ClientForm()
    return render(request, 'agenda/client_form.html', {'form': form})


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = AppointmentForm()
    return render(request, 'agenda/appointment_form.html', {'form': form})

def professional_edit(request, pk):
    professional = get_object_or_404(Professional, pk=pk)

    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=professional)
        if form.is_valid():
            form.save()
            return redirect('agenda:professional_list')
    else:
        form = ProfessionalForm(instance=professional)

    return render(request, 'agenda/professional_edit.html', {'form': form})


def professional_delete(request, pk):
    professional = get_object_or_404(Professional, pk=pk)

    if request.method == 'POST':
        professional.delete()
        return redirect('agenda:professional_list')

    return render(request, 'agenda/professional_confirm_delete.html', {'professional': professional})