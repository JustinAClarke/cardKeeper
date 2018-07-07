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
from django.conf.urls import url

from . import views

app_name = 'cardKeeper'

urlpatterns = [
    # ex: /recipe/
    url(r'^$', views.index, name='index'),

#    admin_home
    url(r'^admin/$', views.admin_home, name='admin_home'),

#    admin_cards
#    url(r'^admin_cards/(?P<project_id>[0-9]+)/$', views.admin_cards, name='admin_cards'),
#    url(r'^admin_cards/$', views.admin_cards, name='admin_cards'),

#    card_wrangle
    url(r'^card_wrangle/(?P<project_id>[0-9]+)/(?P<card_id>[0-9]+)/$', views.card_wrangle, name='card_wrangle'),
    url(r'^card_wrangle/(?P<project_id>[0-9]+)/$', views.card_wrangle, name='card_wrangle'),

#    card_add
    url(r'^card_add/(?P<project_id>[0-9]+)/$', views.card_add, name='card_add'),
    
#    card save, add another?
    url(r'^card_saved/(?P<project_id>[0-9]+)/(?P<card_id>[0-9]+)/$', views.card_saved, name='card_saved'),

#    admin_projects
#    url(r'^admin_projects/$', views.admin_projects, name='admin_projects'),

#    projects_add_edit
    url(r'^projects_add_edit/(?P<project_id>[0-9]+)/$', views.projects_add_edit, name='projects_add_edit'),
    url(r'^projects_add_edit/$', views.projects_add_edit, name='projects_add_edit'),

]
