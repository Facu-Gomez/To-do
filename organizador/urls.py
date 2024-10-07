from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path


app_name = 'organizador'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = "home"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(template_name="organizador/logout.html"), name="logout"),
    path('<int:pk>/editar', views.edit_profile, name='editar_perfil'),
    #urls facultad:
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/completar/', views.completar_tarea, name='completar_tarea'),
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    #urls trabajo:
    path('trabajo/', views.lista_trabajo, name='lista_trabajo'),
    path('trabajo/crear/', views.crear_trabajo, name='crear_trabajo'),
    path('trabajo/<int:trabajo_id>/completar/', views.completar_trabajo, name='completar_trabajo'),
    path('trabajo/<int:trabajo_id>/editar/', views.editar_trabajo, name='editar_trabajo'),
    path('trabajo/<int:trabajo_id>/eliminar/', views.eliminar_trabajo, name='eliminar_trabajo'),
    #urls notas:
    path('notas/crear/', views.crear_notas, name='crear_notas'),
    path('notas/<int:notas_id>/editar/', views.editar_notas, name='editar_notas'),
    path('notas/<int:notas_id>/eliminar/', views.eliminar_notas, name='eliminar_notas'),
]

