from django.shortcuts import render
from .models import ProfileInfo

# Create your views here.


def index(request):
    """View for the home page"""

    return render(request, 'pdf/accept.html')