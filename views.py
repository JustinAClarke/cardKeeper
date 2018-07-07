"""
    Django Card Keeper Justin Fuhrmeister-Clarke, a media card logger.
    Copyright (C) 2018  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

from django.conf import settings

from .models import Project, Card

from .forms import ProjectForm, CardForm, WrangledForm

def getTitle(title=False):
    string = ""
    try:
        string = settings.SITE_TITLE
    except:
        string = "Card Keeper"
    if(title):
        string += " - " + title
    return string


def index(request):
    projects = Project.objects.all().order_by('id').reverse()
    
    context = {'title': getTitle(), 'request': request, 'projects':projects}
    return render(request, 'cardKeeper/index.html', context)

def admin_home(request):
    projects = Project.objects.all().order_by('id').reverse()
    
    context = {'title': getTitle("Admin"), 'request': request, 'projects':projects}
    return render(request, 'cardKeeper/admin_home.html', context)

def admin_cards(request,project_id=-1):
    projects = Project.objects.all().order_by('Title')
    project=false
    if project_id != -1:
        project = get_object_or_404(Project, pk=project_id)
    context = {
        'title': getTitle(),
        'request': request,
        'projects': projects,
        'project': project,
        }
    return render(request, 'cardKeeper/admin_cards.html', context)

def card_wrangle(request,project_id,card_id=-1):
    project = get_object_or_404(Project, pk=project_id)
    card=[]
    card_form=[]
    template='cardKeeper/admin_cards.html'
    if card_id != -1:
        card = get_object_or_404(Card, pk=card_id)
        template='cardKeeper/card_wrangle.html'
        if request.method == "POST":
            card_form = WrangledForm(request.POST, instance=card) # A form bound to the POST data
            if card_form.is_valid(): # All validation rules pass
                #set project and  'project_card_id', save to card, return ID
                new_card = card_form.save()

                return HttpResponseRedirect(reverse('cardKeeper:card_wrangle', args=(project_id)))
        else:
            title=getTitle("Wrangle Card")
            card_form = WrangledForm(instance=card)
            
    context = {'title': getTitle(), 'request': request, 'project':project, 'card':card, 'form':card_form}
    return render(request, template, context)

def card_add(request,project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        card_form = CardForm(request.POST) # A form bound to the POST data
        if card_form.is_valid(): # All validation rules pass
            #set project and  'project_card_id', save to card, return ID
            new_card = card_form.save()
            new_card.project_obj=project
            running_count = project.card_set.all().count()
            new_card.card_id=running_count + 1
            new_card.save()
            return HttpResponseRedirect(reverse('cardKeeper:card_saved', args=(project_id,new_card.card_id)))
    else:
        title=getTitle("Add Card")
        card_tmp=Card()
        card_tmp.project_obj_id=project_id
        card_form = CardForm(instance=card_tmp)
    context = {'request':request,'form':card_form,'title':title, 'project':project}
    return render(request, 'cardKeeper/card_add.html', context)

def card_saved(request, project_id, card_id):
    context = {'request': request, 'project_id': project_id, 'card_id': card_id, 'title': getTitle("Card; {} Saved".format(card_id))}
    return render(request, 'cardKeeper/card_saved.html', context)

def admin_projects(request):
    projects = Project.objects.all().order_by('id').reverse()
    
    context = {'title': getTitle(), 'request': request,'projects':projects}
    return render(request, 'cardKeeper/admin_projects.html', context)

def projects_add_edit(request,project=-1):
    if request.method == "POST":
        project_form = ProjectForm(request.POST) # A form bound to the POST data
        if project_form.is_valid(): # All validation rules pass
            new_project = project_form.save()
            return HttpResponseRedirect(reverse('cardKeeper:projects_add_edit'))
    else:
        if project != -1:
            project = get_object_or_404(Project, pk=project)
            title=getTitle("Edit Project")
            project_form = ProjectForm(instance=project)
            form_method="Update"
        else:
            title=getTitle("Add Project")
            project_form = ProjectForm()
            form_method="Add"
    context = {'request':request,'form':project_form,'title':title,'form_method':form_method}

    return render(request, 'cardKeeper/projects_add_edit.html', context)
