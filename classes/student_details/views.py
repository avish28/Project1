from django.shortcuts import render

# Create your views here.

def student_details(request):
    return render(request,'templates/student_details/student_details_html.html',)
