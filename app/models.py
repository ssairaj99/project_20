from django.db import models

# Create your models here.

class Country(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    cpl=models.IntegerField()
    def __str__(self):
        return str(self.cid)

class State(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    spl=models.IntegerField()
    cid=models.ForeignKey(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.sname