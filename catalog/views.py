from django.shortcuts import render

<<<<<<< homework-branch
def index(request):
    return render(request, 'catalog/index.html')
=======
def home(request):
    return render(request, 'catalog/home.html')

>>>>>>> develop

def contacts(request):
    return render(request, 'catalog/contacts.html')
