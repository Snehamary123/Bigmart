from django.urls import path
from webapp import views

urlpatterns=[path('',views.homepage,name='home'),
path('about/',views.aboutpage,name='about'),
path('contact/',views.contactpage,name='contact'),
path('product/',views.ourproductpage,name='product'),
path('savecontact/',views.savecontact,name='savecontact'),
path('pdtsfiltered/<catname>/',views.pdtsfiltered,name='pdtsfiltered'),
path('singlepdtpage/<int:proid>/',views.singlepdtpage,name='singlepdtpage'),
path('savecartpage/',views.savecartpage,name='savecartpage'),
path('cartpage/',views.cartpage,name='cartpage'),
path('delete_item/<int:p_id>/',views.delete_item,name='delete_item'),





path('loginform/',views.loginform,name='loginform'),
path('signupform/',views.signupform,name='signupform'),
path('savesignupform/',views.savesignupform,name='savesignupform'),
path('userlogin/',views.userlogin,name='userlogin'),
path('logout/',views.logout,name='logout'),

             ]