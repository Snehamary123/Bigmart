from django.shortcuts import render,redirect
from backend.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contactdb
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req,'index.html')
def categorypage(req):
    return render(req,'category.html')
def savecategory(req):
    if req.method=='POST':
        na=req.POST.get('name')
        des = req.POST.get('descript')
        img=req.FILES['pic']
        obj=categorydb(category_name=na,description=des,category_img=img)
        obj.save()
        messages.success(req,"successfully saved category...!")
        return redirect(categorypage)
def dispalycategorypage(req):
    data=categorydb.objects.all()
    return render(req,'displaycategory.html',{'data':data})
def editcategory(req,catid):
    data=categorydb.objects.get(id=catid)
    return render(req,'editcategory.html',{"data":data})
def updatecategory(req,catid):
    if req.method=='POST':
        na=req.POST.get('name')
        des = req.POST.get('descript')
        try:
            img=req.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=catid).category_img
        categorydb.objects.filter(id=catid).update(category_name=na,description=des,category_img=file)
        return redirect(dispalycategorypage)
def deletecategory(req,catid):
    x=categorydb.objects.filter(id=catid)
    x.delete()
    messages.warning(req, "deleted category...!")

    return redirect(dispalycategorypage)
#********************************************************************************************************************
def adminloginpage(req):
    return render(req,'adminlogin.html')
def saveadmin_login(req):
    if req.method == 'POST':
        us = req.POST.get('user')
        ps = req.POST.get('pswd')
        if User.objects.filter(username__contains=us).exists():
            x=authenticate(username=us,password=ps)
            if x is not None:
                login(req,x)
                req.session['username']=us
                req.session['password'] = ps
                messages.success(req, "welcome...!")
                return redirect(indexpage)
            else:
                messages.error(req, "invalid password...!")
                return redirect(adminloginpage)
        else:
            messages.warning(req, " user not found...!")
            return redirect(adminloginpage)

def logoutpage(req):
    del req.session['username']
    del req.session['password']
    return redirect (adminloginpage)


# def signuppage(req):
#     return render(req,'signup.html')
#************************************************************************************************************************************


def productpage(req):
    cat=categorydb.objects.all()
    return render(req,'products.html',{'cat':cat})
def saveproduct(req):
    if req.method=='POST':
        catpdt = req.POST.get('catpdt')
        pdtna = req.POST.get('pdtname')
        pdtpr = req.POST.get('pdtprice')
        pdtdes = req.POST.get('pdtdescript')
        pdtimg=req.FILES['pdtpic']
        obj=productdb(product_category=catpdt,product_name=pdtna,product_price=pdtpr,product_description=pdtdes,product_img=pdtimg)
        obj.save()
        messages.success(req, "successfully saved category...!")
        return redirect(productpage)

def displaypdtpage(req):
    pdtdata=productdb.objects.all()
    return render(req,'displayproducts.html',{'pdtdata':pdtdata})

def editproduct(req,pdtid):
    cat=categorydb.objects.all()
    pdtdata=productdb.objects.get(id=pdtid)
    return render(req,'editproduct.html',{"pdtdata":pdtdata,"cat":cat})

def deletepdt(req,pdtid):
    x=productdb.objects.filter(id=pdtid)
    x.delete()
    messages.warning(req, "deleted products...!")

    return redirect(dispalycategorypage)
# *****************************************************************************************************
def dispalycontact(req):
    contdata=contactdb.objects.all()
    return render(req,'contactdata.html',{'contdata':contdata})

#****************************************************************************************************************



