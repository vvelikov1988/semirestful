from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows

def index(request):
    return render(request, 'index.html')

def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        new_show = Shows.objects.create(
            title=request.POST['title'], 
            network=request.POST['network'], 
            release_date = request.POST['reldate'], 
            description = request.POST['desc'])
        
    return redirect (f'/shows/{new_show.id}')

def showdetails(request, show_id):
    show = Shows.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, 'showdetails.html', context)

def allshows(request):
    shows = Shows.objects.all()
    context = {
        'shows': shows
    }
    return render(request, 'shows.html', context)

def update(request, show_id):
        # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{show_id}/edit')
    else:
        show_update = Shows.objects.get(id=show_id)
        show_update.title=request.POST['title']
        show_update.network=request.POST['network']
        show_update.release_date = request.POST['reldate'] 
        show_update.description = request.POST['desc']
        show_update.save()
        messages.success(request, "Show successfully updated")
        # redirect to a success route
        return redirect (f'/shows/{show_id}')


def editshow(request, show_id):
    
    show = Shows.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, 'editshow.html', context)

def destroy(request, show_id):
    show_delete = Shows.objects.get(id = show_id)
    show_delete.delete()
    return redirect('/shows')




















































































































































































































































































