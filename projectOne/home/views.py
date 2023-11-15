from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact(name=name, surname=surname, username=username, city=city, state=state, zip=zip)
        contact.save()
        messages.warning(request, "User added successfully.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")