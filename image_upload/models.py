from django.db import models
from django.conf import settings

from PIL import Image

import uuid
import os

# Create your models here.


def create_thumbnail(input_image, thumbnail_size=(256, 256,)):
	if not input_image or input_image == '':
		return None

	image = Image.open(input_image)
	image.thumbnail(thumbnail_size, Image.ANTIALIAS)

	filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
	arrdata = filename.split(".")

	extension = arrdata.pop()
	basename = "".join(arrdata)

	new_filename = "{}_thumb.{}".format(basename, extension)

	image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

	return new_filename

def scramble_uploaded_filename(instance, filename):
	extension = filename.split(".")[-1]
	return "{}.{}".format(uuid.uuid4(), extension)

class UploadImage(models.Model):
	title = models.CharField("Title of the uploaded image", max_length=200, default="Unknown Picture")
	description = models.TextField("Description of the uploaded image", default="")
	image = models.ImageField('Uploaded image', upload_to=scramble_uploaded_filename)
	thumbnail = models.ImageField("Thumbnail of the uploaded image", blank=True)

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.thumbnail = create_thumbnail(self.image)

		super(UploadImage, self).save()

	def __str__(self):
		return self.title