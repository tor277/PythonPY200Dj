from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from landing.forms import TemplateFormBook


# Create your views here.
class TemplViewBook(View):

    def get(self, request):
        return render(request, 'landing/index.html')

    def post(self, request):
        received_data = request.POST

        form = TemplateFormBook(received_data)  # Передали данные в форму
        if form.is_valid():
            return JsonResponse(form.cleaned_data, json_dumps_params={'ensure_ascii': False,
                                                                      'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})

def index_view_l(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
