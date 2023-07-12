from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from .models import Patient

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

# def psyco(request):
#     return render(request, 'pages_main/new_patient.html')


# @login_required
# def recipe_rslt (request):
#     form = TestForm(request.POST)
#     return render(request, 'pages_main/final_recipe.html', context = form.resultat)

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def create_patient(request):
    if request.method == 'POST':
        firstname = request.POST.get('patient-firstname')
        lastname = request.POST.get('patient-lastname')
        password = request.POST.get('patient-password')
        
        patient = Patient.objects.create(nom=lastname, prenom=firstname, password=password)
        patient.save()
        
        # Redirigez vers une autre page ou effectuez une autre action
        # Redirigez vers une autre page en utilisant un lien avec href
        return render(request, 'pages_main/redirect_home.html')
    else:
        return render(request, 'pages_main/new_patient.html')

