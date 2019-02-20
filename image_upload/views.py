from django.shortcuts import render
from rest_framework import viewsets
from .models import UploadImage
from .serializers import UploadImageSerializer

# Create your views here.

def index(request):
	template = 'index.html'
	return render(request, template)


class UploadImageViewSet(viewsets.ModelViewSet):
	queryset = UploadImage.objects.all()
	serializer_class = UploadImageSerializer
