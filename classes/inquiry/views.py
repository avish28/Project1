from django.shortcuts import render

# Create your views here.

def inquiry(request):
    return render(request,"templates/inquiry/inquiry_html.html")
