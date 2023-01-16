from django.shortcuts import render,redirect
from django.urls import reverse
from . import models

# Create your views here.
def add(request):
    
        return render(request,'registration/add.html')


def list(request):
    all_students=models.student.objects.all().order_by('roll_no').values()
    context={
        'all_students':all_students
    }
    return render(request,'registration/list.html',context)
