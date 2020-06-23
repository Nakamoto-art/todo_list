from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.index),
    path('tasks/<int:id>/', views.task_detail),
    path('tasks/<int:id>/delete/', views.delete_task),
    path('tasks/<int:id>/update/', views.update_task),
    path('create/', views.create_task),
]