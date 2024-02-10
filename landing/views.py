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
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Получение IP
        else:
            ip = request.META.get('REMOTE_ADDR')  # Получение IP

        user_agent = request.META.get('HTTP_USER_AGENT')
        form = TemplateFormBook(received_data)  # Передали данные в форму
        if form.is_valid():
            return JsonResponse(form.cleaned_data | {'ip': ip, 'user_agent': user_agent},
                                json_dumps_params={'ensure_ascii': False, 'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})


def index_view_l(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
