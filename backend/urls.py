from django.urls import path
from backend import views

urlpatterns=[path('indexpage/',views.indexpage,name='indexpage'),
             path('categorypage/',views.categorypage,name='categorypage'),
             path('savecategory/', views.savecategory, name='savecategory'),
             path('dispalycategorypage/', views.dispalycategorypage, name='dispalycategorypage'),
             path('editcategory/<int:catid>/', views.editcategory, name='editcategory'),
              path('updatecategory/<int:catid>/', views.updatecategory, name='updatecategory'),
             path('deletecategory/<int:catid>/', views.deletecategory, name='deletecategory'),

             path('adminloginpage/', views.adminloginpage, name='adminloginpage'),
             path('logoutpage/', views.logoutpage, name='logoutpage'),
             path('adminloginpage/', views.adminloginpage, name='adminloginpage'),
             # path('signuppage/', views.signuppage, name='signuppage'),

            path('productpage/', views.productpage, name='productpage'),
             path('saveproduct/', views.saveproduct, name='saveproduct'),
             path('displaypdtpage/', views.displaypdtpage, name='displaypdtpage'),
             path('editproduct/<int:pdtid>/', views.editproduct, name='editproduct'),
             path('deletepdt/<int:pdtid>/', views.deletepdt, name='deletepdt'),


             path('dispalycontact/', views.dispalycontact, name='dispalycontact'),

             ]