from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.utils.decorators import method_decorator
from django.db.models import Q

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


# Collections view
def collections(request):
    queryset = Artisan.objects.all()  # .order_by('-timestamp')

    query = request.GET.get("q")

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        ).distinct()  # Disallowed duplicate items

    context = {

        "artisans": queryset,

    }

    return render(request, 'collections.html', context)


def photo_detail(request, slug):
    artisan = get_object_or_404(Artisan, slug=slug)

    return render(request, 'photo_detail.html', {'artisan': artisan})


class ArtisanCreate(LoginRequiredMixin, CreateView):
    model = Artisan
    fields = [
        'title',
        'category',
        'image',
        'description',
        'detail'
    ]

    login_url = '/login/'






