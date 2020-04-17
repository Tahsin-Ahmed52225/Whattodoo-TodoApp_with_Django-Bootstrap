from django.db import models
#Creating model
class Todo(models.Model) :
    date = models.DateTimeField()
    text = models.CharField(max_length = 200)

