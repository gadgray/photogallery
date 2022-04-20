from django.core.checks import messages
from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image

# Create your views here.

def index(request):
    post= Image.objects.all()



    return render(request, 'index.html', {'post': post})


def upload(request):
    if request.method == 'POST':
        image= Image()
        image.name= request.POST.get('title')
        image.description= request.POST.get('description')

        if len(request.FILES) != 0:
            image.image= request.FILES['image']

        image.save()
        messages.success(request, 'image added successfully')
        return redirect('/')

    else:
        return render(request, 'upload.html')

