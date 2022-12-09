from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        info = Contact(name=name, email=email, phone=phone, message=message)
        info.save()
        pix = Images(image=image)
        pix.save()

    return render(request, 'home.html')

def dashboard(request):
    crm = Contact.objects.all()
    context = {
        'all': crm
    }
    return render(request, 'admin.html', context)

def update(request, id):
    tel = Contact.objects.get(id=id)
    if request.method == 'POST':
        tel.name = request.POST.get('name')
        tel.email = request.POST.get('email')
        tel.phone = request.POST.get('phone')
        tel.message = request.POST.get('message')
        image = request.POST.get('image')
        tel.save()
    return redirect('/dashboard')

    context ={
        'call': tel
            }
    return render(request, 'update.html', context)

def delete(request, id):
    dels = Contact.objects.get(id=id)
    dels.delete()
    return redirect('/dashboard')

def pricing(request):
    return render(request, 'pricing.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')