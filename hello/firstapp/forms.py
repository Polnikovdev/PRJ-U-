from django.shortcuts import render
from django import forms
#def index(request):
#    userform = UserForm()
#    return render(request, "firstapp/index.html",
#            {"form": userform})

from django import forms
class UserForm(forms.Form):
   name = forms.CharField(label="Имя клиента",
                          widget=forms.TextInput(attrs={"class": "myfield"}))
   age = forms.IntegerField(label="Возраст клиента",
                            widget=forms.NumberInput(attrs={"class": "myfield"}))