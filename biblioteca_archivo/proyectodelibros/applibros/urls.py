from django.urls import path
from . import views
app_name='applibros'
urlpatterns = [
    path('', views.index, name='index'),
    path('libros/<int:libro_id>', views.detail, name='detail'),
    path('add/', views.add_libro, name='add_libro'),
    path('update/<int:id>/', views.update, name='update'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar')
]