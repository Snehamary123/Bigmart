from django.db import models

# Create your models here.
class categorydb(models.Model):
    category_name=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(max_length=100,blank=True,null=True)
    category_img=models.ImageField(upload_to='categorypics',blank=True,null=True)

class productdb(models.Model):
    product_category=models.CharField(max_length=100,blank=True,null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)

    product_description=models.TextField(max_length=100,blank=True,null=True)
    product_img = models.ImageField(upload_to='productspics', blank=True, null=True)

class registerationdb(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)

    profilepic = models.ImageField(upload_to='profilepics', blank=True, null=True)
