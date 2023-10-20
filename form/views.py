from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FormSerializer
from .models import Form
from django.http import HttpResponse
from django.conf import settings
from django.contrib.staticfiles.views import serve

class FormView(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    queryset = Form.objects.all()
