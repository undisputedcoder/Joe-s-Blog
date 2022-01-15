"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Articles

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    articles = Articles.objects.all()
    return render(
        request,
        'app/index.html',
        {'articles': articles}
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    articles = Articles.objects.all()
    return render(
        request,
        'app/contact.html',
        {
            'article': articles
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
