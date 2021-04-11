from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus, Student
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm
from django.urls import reverse

def updateStudent(request, student_id):
    print('test')