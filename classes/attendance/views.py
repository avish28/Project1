from django.shortcuts import render

# Create your views here.

def attendance(request):
    return render(request,"templates/attendance/attendance_html.html")
