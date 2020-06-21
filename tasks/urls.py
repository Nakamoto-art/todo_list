from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.task_list_view, name='index'),
    path('tasks/<int:id>/', views.task_detail, name='index'),
    path('tasks/<int:id>/delete/', views.delete_task),
    path('create/', views.create_task, name='create_task'),
]