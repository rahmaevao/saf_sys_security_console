from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
import re
from django.views.generic import ListView

from main_app.models import Premises


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Premises

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def about(request):
    return render(request, "main_app/about.html")


def contact(request):
    return render(request, "main_app/contact.html")
