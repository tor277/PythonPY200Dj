from django.urls import path

from landing.views import index_view_l, TemplViewBook

app_name = 'landing'


urlpatterns = [
    path('', TemplViewBook.as_view(), name='index'),
]