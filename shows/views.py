from django.shortcuts import render, HttpResponse, redirect
from . import models

def index(request):
    return render(request, 'index.html')

# def create(request, show_id):
#     Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date = request.POST['reldate'], description = request.POST['desc'])
#     return redirect,(f'/shows/{show_id}')

# def showdetails(request, show_id):
#     return redirect('/')