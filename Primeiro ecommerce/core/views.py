from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    texts= ["Lorem ipsum dolor sit amet, consectetur adipisicing elit"]

    context = {
        "title" : "django e-commerce",
        "texts" : texts
    }
    return render(request,"index.html",context)



