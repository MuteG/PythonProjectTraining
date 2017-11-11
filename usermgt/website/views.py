from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html')


def login(request):
    template = get_template('login.html')
    html = template.render()
    return HttpResponse(html)


def register(request):
    return render_to_response('register.html')


def forgotpassword(request):
    return render_to_response('forgot-password.html')
