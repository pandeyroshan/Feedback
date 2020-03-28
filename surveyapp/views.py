from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from surveyapp.forms import surveyform
# Create your views here.

@csrf_exempt
def home(request):
    return render(request,'index.html')



@csrf_exempt
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        User.objects.create_user(username=username,password=password)
        return HttpResponseRedirect('/home')  



@csrf_exempt
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            return HttpResponseRedirect('/main')

@csrf_exempt
def main(request):
    form=surveyform()
    return render(request,'main.html',{'form':form})        

@csrf_exempt
def collect(request):
    if request.method=='POST':
        form=surveyform(request.post)
        form.save()
        return HttpResponseRedirect('/main')
    
   





    