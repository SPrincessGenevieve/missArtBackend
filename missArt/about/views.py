from django.shortcuts import render


from rest_framework import viewsets


from .serializers import AboutSerializer


from .models import About


class AboutView(viewsets.ModelViewSet):


	serializer_class = AboutSerializer
	queryset = About.objects.all()
