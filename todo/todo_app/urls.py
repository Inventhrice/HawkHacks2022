from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('index/', views.todo_app_view)
]