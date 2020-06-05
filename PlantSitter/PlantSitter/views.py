from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# Home page for website
class Home(View):
  def get(self, request, *args, **kwargs):
    return render(request, "home.html")
