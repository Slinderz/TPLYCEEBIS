from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus, Student, Presence
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm, PresenceForm
from django.urls import reverse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import datetime


# Create your views here.
# def index(request):
#  return HttpResponse("Racine de lycée")

def detail(request, cursus_id):
    context = {}
    # Récupération nom formation
    cursus_name = Cursus.objects.get(id=cursus_id)
    context['cursus_name'] = cursus_name
    # Récupération des élèves
    result_student_cursus = Student.objects.filter(cursus_id=cursus_id)

    url = request.get_full_path_info()
    parsed = parse_qs(urlparse.urlparse(url).query)

    if len(parsed) > 0:
        listCall = []
        date = ''
        for x in parsed.keys():
            if x == 'date':
                date = parsed[x][0]
            else:
                listCall.append(parsed[x][0])

        for x in result_student_cursus:
            missing = True
            newRoll = Presence()
            newRoll.date = date
            newRoll.student_id = x.id
            if newRoll.student_id in parsed:
                newRoll.isMissing = True
            else:
                newRoll.isMissing = False
            newRoll.save()

    array = []
    for x in result_student_cursus:
        array.append({'first_name': x.first_name, 'last_name': x.last_name, 'id': x.id})

    context['student'] = array
    return render(request, 'lycee/listStudent.html', context)


def index(request):
    result_list = Cursus.objects.all()
    context = {
        'liste': result_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'lycee/index.html', context)


def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    url = request.get_full_path_info()
    parsed = parse_qs(urlparse.urlparse(url).query)
    if len(parsed) > 0:
        result_list.last_name = parsed['lname'][0]
        result_list.first_name = parsed['fname'][0]
        result_list.birth_date = parsed['birth'][0]
        result_list.email = parsed['mail'][0]
        result_list.cursus_id = parsed['cursus'][0]
        result_list.comment = parsed['comments'][0]
        result_list.save()

    context = {
        'liste': result_list
    }
    return render(request, 'lycee/student/detail_student.html', context)


def edit_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    cursus = Cursus.objects.all()
    list_cursus_name = []
    for x in cursus:
        list_cursus_name.append({'name': x.name, 'id': x.id})
    context = {
        'liste': result_list,
        'listeCursus': list_cursus_name
    }
    return render(request, 'lycee/student/edit_student.html', context)


def call_of_roll_cusus(request, cursus_id):
    context = {}
    date = datetime.today().strftime('%Y-%m-%d')
    list_student = Student.objects.filter(cursus_id=cursus_id)
    context['students'] = list_student
    context['date'] = date
    context['cursus_id'] = cursus_id
    return render(request, 'lycee/cursus/call_of_roll.html', context)


class StudentCreateView(CreateView):
    model = Student
    # Formulaire
    form_class = StudentForm
    # Template
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse('detail_student', args=(self.object.pk,))


class CallOfRoll(CreateView):
    model = Presence
    # Formulaire
    form_class = PresenceForm
    # Template
    template_name = 'lycee/cursus/particular_call_of_roll.html'

    def get_success_url(self):
        print('test')
        return reverse('index')
