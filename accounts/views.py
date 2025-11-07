from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
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
