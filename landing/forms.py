from django import forms


class TemplateFormBook(forms.Form):
    my_name = forms.CharField()
    my_email = forms.EmailField()
