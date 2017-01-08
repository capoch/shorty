from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import ShortyURL
from .forms import SubmitUrlForm

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Shorty.ch",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)
    def post(self, request, *args, **kwargs):
        print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            "title": "Shorty.ch",
            "form": form
        }
        return render(request, "shortener/home.html", context)


class ShortyCBView(View):
    meta = ShortyURL
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortyURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
