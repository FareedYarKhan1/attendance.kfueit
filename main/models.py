from datetime import date
from email.policy import default
import imp
from tabnanny import check
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class attendance(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    check_in=models.DateTimeField(default=None,null=True,blank=True)
    check_out=models.DateTimeField(default=None,null=True,blank=True)

    def __str__(self) -> str:
        return "attendance-"+str(self.employee.first_name+" "+ self.employee.last_name)+"-"+str(self.date)
    