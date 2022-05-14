from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('', views.todo_app_view),
    path('addTodoItem/', views.addTodo)
]