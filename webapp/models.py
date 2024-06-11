from django.db import models

# Create your models here.
class contactdb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    Message = models.TextField(max_length=100, blank=True, null=True)

class registerdb(models.Model):
        username = models.CharField(max_length=100, blank=True, null=True)
        email = models.EmailField(max_length=100, blank=True, null=True)
        password = models.CharField(max_length=100,blank=True, null=True)
        image = models.ImageField(upload_to='registerationpics', blank=True, null=True)


class cartdb(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    productname = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    Totalprice = models.IntegerField(blank=True, null=True)

class orderdb(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    totalprice = models.IntegerField(blank=True, null=True)
    feedback = models.CharField(max_length=100, blank=True, null=True)



