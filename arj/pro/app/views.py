from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages, auth

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from .models import Shoes
# Create your views here.
def index(request):
    content=Shoes.objects.all()
    data={
        'result':content
    }
    return render(request,'home.html',data)
    