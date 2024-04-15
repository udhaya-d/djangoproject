from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.
con = pymongo.MongoClient("mongodb+srv://udhayakumar6745:root@cluster0.09jj1qn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mydb=con["book"]
mycol=mydb['bookdetails']
def library(request):
    # return HttpResponse("<h1>welcome to home page</h1>")
    return render(request, "library.html")


def homepage(req):
    # return HttpResponse("homepage.html")
    return render(req, "homepage.html")


def newadd(ne):
    # return HttpResponse("<h1>About System</h1>")
    return render(ne, "newadd.html")


def update(up):
    # return HttpResponse("<h1> Raja.C</h1>")
    return render(up, "update.html")


def delete(de):
    # return HttpResponse("<h1> Raja.C</h1>")
    return render(de, "delete.html")


def indexPage(req):
    return render(req, "index.html")
