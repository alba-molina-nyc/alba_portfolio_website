from django.db.models import fields
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Contact
from .models import Quote
from .models import Portfolio
from .models import Blog
from .forms import ContactForm
from .forms import QuoteForm
from main_app import models

def portfolios_index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolios/index.html', { 'portfolios': portfolios })

def portfolios_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    return render(request, 'portfolios/detail.html', { 'portfolio': portfolio })

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', { 'blogs': blogs })

def bletail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'bletail.html', { 'blog': blog })

def home(request):
    return render(request, 'home.html')

def tldr(request):
    return render(request, 'tldr.html')

def tutoring(request):
    return render(request, 'tutoring.html')

def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = QuoteForm()
    context = { 'form': form }
    return render(request, 'quote.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    form = ContactForm()
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')  


