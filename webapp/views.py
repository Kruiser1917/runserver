from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'webapp/index.html')

def catalog(request):
    return render(request, 'webapp/catalog.html')

def category(request):
    return render(request, 'webapp/category.html')

def contacts(request):
    return render(request, 'webapp/contacts.html')


def contacts_page(request):
    return render(request, 'webapp/contacts.html')