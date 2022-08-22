from django.db import models
from django.utils.timezone import now

class Todolist(models.Model):
    mylist=models.CharField(max_length=50)
    mytime=models.DateTimeField(default=now)
    def __str__(self):
        return self.mylist
    

