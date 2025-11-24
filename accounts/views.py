from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm, ProfileForm, UserEditForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('agenda:home')  
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
    user = request.user
    profile = user.profile  # creado automáticamente por la señal

    if request.method == "POST":
        form_user = UserEditForm(request.POST, instance=user)
        form_profile = ProfileForm(request.POST, request.FILES, instance=profile)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect("perfil")
    else:
        form_user = UserEditForm(instance=user)
        form_profile = ProfileForm(instance=profile)

    return render(request, "accounts/perfil.html", {
        "form_user": form_user,
        "form_profile": form_profile
    })

def about(request):
    return render(request, 'agenda/about.html')


# -----------------------------
#        REGISTRO
# -----------------------------
def registro(request):
    if request.method == 'POST':
        form_user = UserRegisterForm(request.POST)
        form_profile = ProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            username = form_user.cleaned_data['username']

            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe.")
                return redirect('registro')

            # Crear usuario → la señal ya crea Profile automáticamente
            user = form_user.save()

            # Actualizar el Profile creado por la señal
            profile = user.profile
            profile.profesion = form_profile.cleaned_data.get('profesion')
            profile.comentario = form_profile.cleaned_data.get('comentario')
            profile.foto = form_profile.cleaned_data.get('foto')
            profile.save()

            messages.success(request, "Usuario creado correctamente.")
            return redirect('login')

        return render(request, 'accounts/registro.html', {
            'form_user': form_user,
            'form_profile': form_profile
        })

    else:
        form_user = UserRegisterForm()
        form_profile = ProfileForm()

        return render(request, 'accounts/registro.html', {
            'form_user': form_user,
            'form_profile': form_profile
        })
