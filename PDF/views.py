from django.shortcuts import render
from .models import ProfileInfo
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.


def index(request):
    """View for the home page"""

    if request.method == 'POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')

        profile = ProfileInfo(name=name, email=email, phone=phone, summary=summary, degree=degree,
                              school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'pdf/accept.html')


def resume(request, id):
    """ View for the resume page"""

    user_profile = ProfileInfo.objects.get(pk=id)

    context = {

        'user_profile': user_profile

    }

    template = loader.get_template('pdf/resume.html')
    html = template.render(context)

    options = {

        'page-size': 'Letter',
        'encoding': "UTF-8",
    }

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\wkhtmltox\bin\wkhtmltopdf.exe")

    pdf = pdfkit.from_string(html, False, options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'

    return response


def listview(request):
    """View for the list page"""

    profiles = ProfileInfo.objects.all()

    context = {

        'profiles': profiles
    }

    return render(request, 'pdf/list.html', context)
