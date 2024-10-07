from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .models import TareaFacultad, TareaTrabajo, Notas
from .forms import TareaFacultadForm, TareaTrabajoForm, NotasForm

def home(request):
    notas = Notas.objects.filter(user=request.user) if request.user.is_authenticated else None
    return render(request, 'organizador/index.html', {'notas':notas})


#funciones y vistas del y para el usuario:

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "organizador/login.html"

    def get_success_url(self):
        return reverse_lazy('home')

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Captura la selección del icono de perfil
            default_profile_pic = request.POST.get('default_profile_pic')
            if default_profile_pic:
                user.default_profile_pic = default_profile_pic
            user.save()
            return redirect('login')  # O la vista a la que quieras redirigir
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'organizador/register.html', {'form': form})

@login_required
def edit_profile(request, pk):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado exitosamente.")
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'organizador/editar_perfil.html', {'form': form})



#funciones y vista de tareas de la facultad:

@login_required
def lista_tareas(request):
    tareas = TareaFacultad.objects.filter(user=request.user)
    return render(request, 'organizador/facultad/lista_tareas.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaFacultadForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user  # Asigna la tarea al usuario logueado
            tarea.save()
            return redirect('lista_tareas')
    else:
        form = TareaFacultadForm()
    return render(request, 'organizador/facultad/crear_tarea.html', {'form': form})

@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(TareaFacultad, id=tarea_id, user=request.user)
    tarea.estado = 'C'  # Cambia el estado a 'Completada'
    tarea.save()
    return redirect('lista_tareas')

@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(TareaFacultad, id=tarea_id, user=request.user)
    
    if request.method == 'POST':
        form = TareaFacultadForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaFacultadForm(instance=tarea)
    
    return render(request, 'organizador/facultad/editar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(TareaFacultad, id=tarea_id, user=request.user)
    tarea.delete()
    return redirect('lista_tareas')



#funciones y vistas para las tareas del trabajo:

@login_required
def lista_trabajo(request):
    trabajos = TareaTrabajo.objects.filter(user=request.user)
    return render(request, 'organizador/trabajo/lista_trabajo.html', {'trabajos': trabajos})

@login_required
def crear_trabajo(request):
    if request.method == 'POST':
        form = TareaTrabajoForm(request.POST)
        if form.is_valid():
            trabajo = form.save(commit=False)
            trabajo.user = request.user 
            trabajo.save()
            return redirect('lista_trabajo')
    else:
        form = TareaTrabajoForm()
    return render(request, 'organizador/trabajo/crear_trabajo.html', {'form': form})


@login_required
def completar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(TareaTrabajo, id=trabajo_id, user=request.user)
    trabajo.estado = 'C' 
    trabajo.save()
    return redirect('lista_trabajo')

@login_required
def editar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(TareaTrabajo, id=trabajo_id, user=request.user)
    
    if request.method == 'POST':
        form = TareaTrabajoForm(request.POST, instance=trabajo)
        if form.is_valid():
            form.save()
            return redirect('lista_trabajo')
    else:
        form = TareaTrabajoForm(instance=trabajo)
    
    return render(request, 'organizador/trabajo/editar_trabajo.html', {'form': form})

@login_required
def eliminar_trabajo(request, trabajo_id):
    trabajo = get_object_or_404(TareaTrabajo, id=trabajo_id, user=request.user)
    trabajo.delete()
    return redirect('lista_trabajo')


#funciones y vistas de las notas

@login_required
def crear_notas(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            notas = form.save(commit=False)
            notas.user = request.user 
            notas.save()
            return redirect('home')
    else:
        form = NotasForm()
    return render(request, 'organizador/notas/crear_nota.html', {'form': form})

@login_required
def editar_notas(request, notas_id):
    notas = get_object_or_404(Notas, id=notas_id, user=request.user)
    
    if request.method == 'POST':
        form = NotasForm(request.POST, instance=notas)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NotasForm(instance=notas)
    
    # Asegúrate de devolver el formulario renderizado
    return render(request, 'organizador/notas/editar_nota.html', {'form': form})

@login_required
def eliminar_notas(request, notas_id):
    notas = get_object_or_404(Notas, id=notas_id, user=request.user)
    notas.delete()
    return redirect('home')