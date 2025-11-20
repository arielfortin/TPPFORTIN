from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.contrib import messages
from .forms import RegistroForm, ProfileExtraForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            #return redirect('dashboard')
            return redirect('agenda:home')   # 👈 Redirige al menú principal
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def usuarios_view(request):
    # Crear usuario
    if request.method == 'POST':
        if 'crear' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                User.objects.create_user(username=username, password=password)

        # Editar usuario
        if 'editar' in request.POST:
            user_id = request.POST['user_id']
            username = request.POST['username']
            user = User.objects.get(id=user_id)
            user.username = username
            if request.POST['password']:
                user.set_password(request.POST['password'])
            user.save()

    # Eliminar usuario
    if request.GET.get('eliminar'):
        user_id = request.GET.get('eliminar')
        User.objects.get(id=user_id).delete()

    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required
def perfil_view(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('perfil')

    return render(request, 'accounts/perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def registro(request):
    if request.method == "POST":
        form_user = RegistroForm(request.POST)
        form_profile = ProfileExtraForm(request.POST)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save(commit=False)
            user.set_password(form_user.cleaned_data["password"])
            user.save()

            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Cuenta creada correctamente.")
            login(request, user)
            return redirect("home")   # Página principal de agenda

    else:
        form_user = RegistroForm()
        form_profile = ProfileExtraForm()

    return render(
        request,
        "accounts/registro.html",
        {
            "form_user": form_user,
            "form_profile": form_profile
        }
    )

def about(request):
    return render(request, 'agenda/about.html')

