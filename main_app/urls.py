from django.urls import path

from . import views


urlpatterns = [
    # we will define all app-level urls in this list
    path('', views.home, name='home'),
    path('tldr', views.tldr, name='tldr'),
    path('tutoring/', views.tutoring, name='tutoring'),
    path('contact/', views.contact, name='contact'),
    path('quote', views.quote, name='quote'),
    path('resume', views.resume, name='resume'),
    path('portfolios/', views.portfolios_index, name='index'),
    path('portfolios/<int:portfolio_id>/', views.portfolios_detail, name='detail'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/', views.bletail, name='bletail'),
   
  
]
