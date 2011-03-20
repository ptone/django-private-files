from django.db import models
from django.contrib.auth.models import User
from private_files import PrivateFileField

class FileSubmission(models.Model):
    description = models.CharField("description", max_length = 200)
    uploaded_file = PrivateFileField("file", upload_to = 'uploads')