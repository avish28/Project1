from django.shortcuts import render

# Create your views here.

def attandance(request):
    return render(request,"attandance/attandace_html.html")
