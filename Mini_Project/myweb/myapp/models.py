from django.db import models
class Employee(models.Model):
    eid=models.CharField(max_length=10)
    ename=models.CharField(max_length=100)
    eemail=models.EmailField(default='')
    econtact=models.CharField(max_length=20)
    def __str__(self):
        return self.ename
        
    
