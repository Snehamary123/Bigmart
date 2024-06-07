from django.shortcuts import render,redirect
from backend.models import productdb,categorydb
from webapp.models import contactdb,registerdb,cartdb
from django.contrib import messages
# Create your views here.
def homepage(req):
    cat=categorydb.objects.all()
    return render(req,'home.html',{'cat':cat})
def aboutpage(req):
    cat=categorydb.objects.all()
    return render(req,'about.html',{'cat':cat})
def contactpage(req):
    cat=categorydb.objects.all()
    return render(req,'contact.html',{'cat':cat})
def ourproductpage(req):
    cat = categorydb.objects.all()
    pro=productdb.objects.all()

    return render(req,'ourproducts.html',{"products":pro,'cat':cat})

def savecontact(req):
    if req.method=='POST':
        nam = req.POST.get('name')
        em = req.POST.get('email')
        ph = req.POST.get('phone')
        sub = req.POST.get('subject')
        Mess = req.POST.get('message')
        obj=contactdb(name=nam,email=em,phone=ph,subject=sub,Message=Mess)
        obj.save()
        return redirect(contactpage)


def pdtsfiltered(req,catname):
    cat=categorydb.objects.all()
    catdata=categorydb.objects.all()
    data=productdb.objects.filter(product_category=catname)
    return render(req,'products_filtered.html',{'data':data,'catdata':catdata,'cat':cat})

def singlepdtpage(req,proid):
    datapr=productdb.objects.get(id=proid)
    cat = categorydb.objects.all()
    return render(req,'singlepdt.html',{'datapr':datapr,"cat":cat})

def savecartpage(req):
    if req.method=="POST":
        qt=req.POST.get('qty')
        tp = req.POST.get('tprice')
        pn = req.POST.get('pdtname')
        un = req.POST.get('username')
        obj=cartdb(username=un,productname=pn,quantity=qt,Totalprice=tp)
        obj.save()
        return redirect(homepage)

def cartpage(req):
    data=cartdb.objects.filter(username=req.session['username'])
    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.Totalprice
        if subtotal>=500:
            shipping_charge=50
        else:
            shipping_charge = 100
        total=subtotal+shipping_charge
    return render(req,'cart.html',{'data':data,'subtotal':subtotal,"total":total,"shipping_charge":shipping_charge})

def delete_item(req,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cartpage)
#**********************************************************


def loginform(req):
    return render(req,'loginform.html')
def signupform(req):
    return render(req,'signupform.html')
def savesignupform(req):
    if req.method=='POST':
        nam = req.POST.get('name')
        em = req.POST.get('email')
        pas = req.POST.get('pass1')
        img = req.FILES['pic']
        obj=registerdb(username=nam,email=em,password=pas,image=img)
        if registerdb.objects.filter(username=nam).exists():
            messages.warning(req,"username already exists")
            return redirect(signupform)
        elif registerdb.objects.filter(email=em).exists():
            messages.warning(req,"email already exists")
            return redirect(signupform)
        else:
            obj.save()
            messages.success(req, "successfully registered")
        return redirect(loginform)


# validating that username and password are same as used into sign up
def userlogin(request):
    if request.method=='POST':
        nam = request.POST.get('uname')
        pswd = request.POST.get('pass')
        if registerdb.objects.filter(username=nam,password=pswd).exists():
           request.session['username'] = nam
           request.session['password'] = pswd
           return redirect(homepage)
        else:
           return redirect(signupform)
    else:
        return redirect(signupform)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginform)