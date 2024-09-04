# views.py
from django.shortcuts import render

def generate_resume(request):
    # Get the user's data from the database or wherever it's stored
    personal_info = ...
    education = ...
    skills = ...
    experience = ...
    projects = ...

    # Render the resume template with the data
    return render(request, 'resume.html', {
        'personal_info': personal_info,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects,
    })


# views.py
import pdfkit

def generate_resume(request):
    # ... (same as before)

    # Render the HTML template to a string
    html_string = render_to_string('resume.html', {
        'personal_info': personal_info,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects,
    })

    # Convert the HTML to PDF
    pdf = pdfkit.from_string(html_string, False)

    # Return the PDF as a response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response