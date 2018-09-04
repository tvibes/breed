from django.shortcuts import render
from django.conf import settings

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect, get_object_or_404  # Look for object that relates to some sought of call.
from django.template import loader

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import Context, Template
from django.template.loader import get_template

from .models import Artisan


# Create your views here.
def home(request):
    return render(request, 'home.html')


def collections(request):
    queryset = Artisan.objects.all()

    context = {

        "artisans": queryset,

    }

    return render(request, 'collections.html', context)
