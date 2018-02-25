from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.forms import forms, ModelForm
from django.http import HttpResponseNotModified
from django.shortcuts import render
from django.shortcuts import resolve_url

from TODO_list.models import todo

class Form(ModelForm):
    class Meta:
        model = todo
        fields = ('title', 'description',)
        
class TaskList(ListView):
    model = todo
    template_name = "TODO_list/list.html"

class TaskAdd(CreateView):
    template_name = 'TODO_list/add.html'
    form_class = TaskForm

    def get_success_url(self):
        return resolve_url('details')

class TaskUpdate(UpdateView):
    model = todo
    fields = "__all__"
    template_name = 'TODO_list/edit.html'
