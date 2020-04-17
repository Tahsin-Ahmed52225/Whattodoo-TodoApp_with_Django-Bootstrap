from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('',include('Todo.urls')),
    path('admin/', admin.site.urls),
    path('button/',include('Todo.urls')),
    path('delete/<int:todo_id>/',include('Todo.urls')),
]