from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('<int:pk>/toggle/', views.toggle_task, name='toggle_task'),
    path('create-cv/', views.create_cv, name='create_cv'),
    path('cv/<int:pk>/', views.view_cv, name='view_cv')
]
