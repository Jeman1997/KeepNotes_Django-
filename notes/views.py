from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Notes
from django.urls import reverse
# Create your views here.
def index(request):
    mynotes=Notes.objects.all().values()
    template=loader.get_template('notes.html')
    context={
    'mynotes':mynotes,
    }
    return HttpResponse(template.render(context,request))
def add(request):
    template=loader.get_template('notes.html')
    ttle=request.POST['title']
    cont=request.POST['content']
    note=Notes(title=ttle,content=cont)
    note.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    note=Notes.objects.get(id=id)
    note.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request,id):
    titlech=request.POST['titlech']
    contentch=request.POST['contentch']
    note=Notes.objects.get(id=id)
    note.title=titlech
    note.content=contentch
    note.save()
    return HttpResponseRedirect(reverse('index'))
