from django.shortcuts import render
from django.views import ListView

# Create your views here.
class SlickTableListView(ListView):
    class Meta:
        abstract = True
        fields: list[str] = []