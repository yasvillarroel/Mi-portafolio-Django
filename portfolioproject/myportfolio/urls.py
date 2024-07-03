from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('caos_news/', views.caos_news, name='caos_news'),
    path('dino/', views.dino, name='dino'),
    path('ayuda_peludo/', views.ayuda_peludo, name='ayuda_peludo'),
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
    
    path('vista_protegida', views.vista_protegida, name='vista_protegida'),

    path('proyecto/<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),  # Nueva URL para el detalle del proyecto
]
 