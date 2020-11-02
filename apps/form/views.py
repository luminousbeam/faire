from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "form/index.html")


def form(request):
    return render(request, 'form/form.html')