from django.urls import path
from . import views


urlpatterns=[
    path('',views.course_view,name='course')
]