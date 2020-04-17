from django.urls import path
from . import views

urlpatterns = [
 #url and hitting the fucntion
    path('',views.index,name='index'),
    path('button/',views.submit,name= "text"),
    path('delete/<int:todo_id>/',views.delete,name="delete"),
]
