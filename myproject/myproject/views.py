from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Message
from .models import Counter

def home(request):
    return HttpResponse(f"Home")

def hello(request, name):
    Message.objects.create(name=name)
    return render(request, 'hello.html', {'name': name})

def stats(request):
    messages = Message.objects.count()
    return render(request, 'stats.html', {'total_greetings': messages})

def stats_name(request, name):
    messages = Message.objects.filter(name=name)
    return render(request, 'stats_name.html', {'greetings': messages, 'name': name})