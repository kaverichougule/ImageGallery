from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
    img = Image.objects.all()
    return render(request,'home.html',{'img':img})


def addimages(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    return render(request, 'addimages.html',{'form':form})

def photo(request):
    return render(request,'photo.html')

def about(request):
    return render(request,'about.html')