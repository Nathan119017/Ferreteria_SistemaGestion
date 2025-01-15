from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from .views import HomeView
from django.views.generic import RedirectView
from factura import views as invoice_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', RedirectView.as_view(url='/register/')),
    
    path('home/', HomeView.as_view(), name="home"),
    
    path('users/',include('users.urls', namespace='users')),
    
    path('products/',include('products.urls', namespace='products')),
    
    path('suppliers/',include('suppliers.urls', namespace='suppliers')),
    
    path('clients/',include('clients.urls', namespace='clients')),
    
    path('register/',include('loginapp.urls', namespace='registerapp')),
    
    path('login/',include('loginapp.loginurl', namespace='loginapp')),
    
    path('logout/',include('loginapp.logouturl', namespace='logoutapp')),

    path('payment_methods/',include('payment_methods.urls', namespace='payment_methods')),

    path('categories/',include('categories.urls', namespace='categories')),

    path('branch_offices/',include('branch_offices.urls', namespace='branch_offices')),

    path('document_type/',include('document_type.urls', namespace='document_type')),

    path('work_schedules/',include('work_schedules.urls', namespace='work_schedules')),

    path('tax/',include('tax.urls', namespace='tax')),

    path('devolucion/',include('devolucion.urls', namespace='devolucion')),

    path('city/',include('city.urls', namespace='city')),

    path('sale/',include('sale.urls', namespace='sale')),

    path('tax_history/',include('tax_history.urls', namespace='tax_history')),

    path('sale_history/',include('sale_history.urls', namespace='sale_history')),

    path('devolucion_history/',include('devolucion_history.urls', namespace='devolucion_history')),

    path('products_history/',include('products_history.urls', namespace='products_history')),

    path('cai/',include('cai.urls', namespace='cai')),

    path('order/',include('order.urls', namespace='order')),
    
    path('productsdetail/',include('productsdetail.urls', namespace='productsdetail')),
    
    path('orderdetail/',include('orderdetail.urls', namespace='orderdetail')),

    path('descuentopromotionapp/',include('descuentopromotionapp.urls', namespace='descuentopromotionapp')),
    
    path('inventory/',include('inventory.urls', namespace='inventory')),

    path('order_history/',include('order_history.urls', namespace='order_history')),
    
    path('', invoice_views.index, name='index'),
    path('invoice/',include('factura.urls')),
]
