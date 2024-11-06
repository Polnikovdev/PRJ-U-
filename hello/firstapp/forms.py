from django.shortcuts import render
from django import forms
#def index(request):
#    userform = UserForm()
#    return render(request, "firstapp/index.html",
#            {"form": userform})

class UserForm(forms.Form):
    file = forms.ImageField(label="Изображение")