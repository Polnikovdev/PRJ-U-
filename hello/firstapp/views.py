from django.shortcuts import render
from django import forms
#from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseGone, HttpResponseServerError
from django.http import *
from django.template.response import TemplateResponse
#from hello.firstapp.forms import UserForm

#class UserForm(forms.Form):
#    file = forms.ImageField(label="Изображение")

#class UserForm(forms.Form):
#    date = forms.DateField(label="Введите дату")

#class UserForm(forms.Form):
#    time = forms.DateField(label="Введите время")

#class UserForm(forms.Form):
#    date_time = forms.DateTimeField(label="Введите дату и время")

#class UserForm(forms.Form):
#    num = forms.IntegerField(label="Введите целое число")

class UserForm(forms.Form):
    num = forms.ChoiceField(label="Выберите язык", choices=((1, "Английский"), (2, "Немецкий"), (3, "Французкий")))

# Create your views here.
def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>" .format(productid, category)
    return HttpResponse(output)
def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3 >" .format(id, name)
    return HttpResponse(output)

def index(request):
    if request.method == "POST":
        name = request.POST.get("form")
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – </h3>".format(name)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})


def about(request):
    #return HttpResponse("About")
    return render(request, "firstapp/about.html")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")




def m304(request):
    return HttpResponseNotModified()
def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")
def m403(request):
    return HttpResponseForbidden ( "<h2>ForЬidden</h2>")
def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")
def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")
def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")