from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import *
from .models import *
from .functions import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4

from django.http import HttpResponse

import pdfkit
from django.template.loader import get_template
import os


#Anonymous required
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = 'dashboard'

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous,
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


def index(request):
    context = {}
    return render(request, 'Factura/CRUD/index.html', context)


@anonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'Factura/CRUD/login.html', context)

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
        

            return redirect('dashboard')
        else:
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')


    return render(request, 'Factura/CRUD/login.html', context)


@anonymous_required
def dashboard(request):
    clients = Client.objects.all().count()
    invoices = Invoice.objects.all().count()
    paidInvoices = Invoice.objects.filter(status='PAID').count()


    context = {}
    context['clients'] = clients
    context['invoices'] = invoices
    context['paidInvoices'] = paidInvoices
    return render(request, 'Factura/CRUD/dashboard.html', context)




@anonymous_required
def invoices(request):
    context = {}
    invoices = Invoice.objects.all()
    context['invoices'] = invoices

    return render(request, 'Factura/CRUD/invoices.html', context)


@anonymous_required
def products(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products

    return render(request, 'Factura/CRUD/products.html', context)



@anonymous_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET':
        form = ClientForm()
        context['form'] = form
        return render(request, 'Factura/CRUD/clients.html', context)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Client Added')
            return redirect('clients')
        else:
            messages.error(request, 'Problem processing your request')
            return redirect('clients')


    return render(request, 'Factura/CRUD/clients.html', context)



@anonymous_required
def logout(request):
    auth.logout(request)
    return redirect('login')


###--------------------------- Create Invoice Views Start here --------------------------------------------- ###

@anonymous_required
def createInvoice(request):
    #create a blank invoice ....
    number = 'INV-'+str(uuid4()).split('-')[1]
    newInvoice = Invoice.objects.create(number=number)
    newInvoice.save()

    inv = Invoice.objects.get(number=number)
    return redirect('create-build-invoice', slug=inv.slug)




def createBuildInvoice(request, slug):
    try:
        invoice = Invoice.objects.get(slug=slug)
    except Invoice.DoesNotExist:
        messages.error(request, 'La factura no existe.')
        return redirect('invoices')

    products = Product.objects.filter(invoice=invoice)

    context = {
        'invoice': invoice,
        'products': products
    }

    if request.method == 'GET':
        prod_form = ProductForm()
        inv_form = InvoiceForm(instance=invoice)
        client_form = ClientSelectForm(initial_client=invoice.client)
        context.update({
            'prod_form': prod_form,
            'inv_form': inv_form,
            'client_form': client_form
        })
        return render(request, 'Factura/CRUD/create-invoice.html', context)

    elif request.method == 'POST':
        prod_form = ProductForm(request.POST)
        inv_form = InvoiceForm(request.POST, instance=invoice)
        client_form = ClientSelectForm(request.POST, initial_client=invoice.client, instance=invoice)

        if prod_form.is_valid():
            obj = prod_form.save(commit=False)
            obj.invoice = invoice
            obj.save()
            messages.success(request, "Producto de factura agregado exitosamente")
            return redirect('create-build-invoice', slug=slug)
        
        elif inv_form.is_valid() and 'paymentTerms' in request.POST:
            inv_form.save()
            messages.success(request, "Factura actualizada exitosamente")
            return redirect('create-build-invoice', slug=slug)
        
        elif client_form.is_valid() and 'client' in request.POST:
            client_form.save()
            messages.success(request, "Cliente agregado a la factura exitosamente")
            return redirect('create-build-invoice', slug=slug)
        
        else:
            context.update({
                'prod_form': prod_form,
                'inv_form': inv_form,
                'client_form': client_form
            })
            messages.error(request, "Problema al procesar su solicitud")
            return render(request, 'Factura/CRUD/create-invoice.html', context)

    return render(request, 'Factura/CRUD/create-invoice.html', context)




def viewPDFInvoice(request, slug):
    # Fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
    except Invoice.DoesNotExist:
        messages.error(request, 'Invoice not found')
        return redirect('invoices')

    # Fetch all the products related to this invoice
    products = Product.objects.filter(invoice=invoice)

    # Get client settings
    p_settings = None

    # Calculate the Invoice Total
    invoiceCurrency = ''
    invoiceTotal = 0.0
    if len(products) > 0:
        for product in products:
            # Check if the product is included in the invoice
            if product.invoice == invoice:
                # Add the price of the product to the invoice total
                y = float(product.price)
                invoiceTotal += y
                invoiceCurrency = product.currency

    # Format the invoice total to two decimal places
    formattedInvoiceTotal = "{:.2f}".format(invoiceTotal)

    context = {
        'invoice': invoice,
        'products': products,
        'p_settings': p_settings,
        'invoiceTotal': formattedInvoiceTotal,
        'invoiceCurrency': invoiceCurrency
    }

    return render(request, 'Factura/CRUD/invoice-template.html', context)




def viewDocumentInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    try:
    # Attempt to get the Settings object with the specified clientName
        p_settings = Settings.objects.get(clientName='Skolo Online Learning')
    # Proceed with your logic using p_settings
    except ObjectDoesNotExist:
    # Handle the case where the Settings object does not exist
    # You can use a default value or None here, depending on your requirements
        p_settings = None 
    

    #Calculate the Invoice Total
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.price)
            invoiceTotal += y



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)

    #The name of your PDF file
    filename = '{}.pdf'.format(invoice.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('Factura/CRUD/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'10', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='C:/Users/jonyg/Documents/PDF/wkhtmltopdf/bin/wkhtmltopdf.exe')

    #IF you have CSS to add to template
    css1 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'bootstrap.min.css')
    css2 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'dashboard.css')

    #Create the file
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    #Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    #Return
    return response



def emailDocumentInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    try:
    # Attempt to get the Settings object with the specified clientName
        p_settings = Settings.objects.get(clientName='Skolo Online Learning')
    # Proceed with your logic using p_settings
    except ObjectDoesNotExist:
    # Handle the case where the Settings object does not exist
    # You can use a default value or None here, depending on your requirements
        p_settings = None 

    #Calculate the Invoice Total
    invoiceTotal = 0.0
    if len(products) > 0:
        for x in products:
            y = float(x.quantity) * float(x.price)
            invoiceTotal += y



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)

    #The name of your PDF file
    filename = '{}.pdf'.format(invoice.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('Factura/CRUD/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'1000', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='C:/Users/jonyg/Documents/PDF/wkhtmltopdf/bin/wkhtmltopdf.exe')

    #Saving the File
    filepath = os.path.join(settings.MEDIA_ROOT, 'client_invoices')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath+filename
    #Save the PDF
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)


    #send the emails to client
    to_email = invoice.client.emailAddress
    from_client = p_settings.clientName
    emailInvoiceClient(to_email, from_client, pdf_save_path)

    invoice.status = 'EMAIL_SENT'
    invoice.save()

    #Email was send, redirect back to view - invoice
    messages.success(request, "Email sent to the client succesfully")
    return redirect('create-build-invoice', slug=slug)







def deleteInvoice(request, slug):
    try:
        Invoice.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    return redirect('invoices')




def companySettings(request):
    company = Settings.objects.get(clientName='Skolo Online Learning')
    context = {'company': company}
    return render(request, 'Factura/CRUD/company-settings.html', context)

    