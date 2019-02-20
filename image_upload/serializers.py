from rest_framework import serializers
from .models import UploadImage


class UploadImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = UploadImage
		fields = ('pk', 'title', 'description', 'image', 'thumbnail', )
		read_only_fields = ('thumbnail', )