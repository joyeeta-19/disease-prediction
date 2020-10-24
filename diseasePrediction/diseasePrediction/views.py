from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")

def result(request):
    aa=joblib.load('finalmodel.sav')
    lis = []
    lis.append(request.GET["symp1"])
    lis.append(request.GET["symp2"])
    lis.append(request.GET["symp3"])
    lis.append(request.GET["symp4"])
    lis.append(request.GET["symp5"])
    if(lis):
        print("yes")
    else:
        print("no")
    return render(request,"result.html")
