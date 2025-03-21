from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Message
from .models import Counter

def home(request):
    return HttpResponse(f"This page has been refreshed x times.")

def hello(request, name):
    Message.objects.create(name=name)
    return HttpResponse(f"Hello, {name}!")

def stats(request):
    messages = Message.objects.count()
    return HttpResponse(f"Greetings: {messages}")

def stats_name(request, name):
    messages = Message.objects.filter(name=name)
    text = "<br>".join([f"{m.name}, {m.created_at}" for m in messages])
    return HttpResponse(f"Greetings:<br>{text}")