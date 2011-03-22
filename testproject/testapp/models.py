from django.db import models
from django.contrib.auth.models import User
from private_files import PrivateFileField, pre_download

class FileSubmission(models.Model):
    description = models.CharField("description", max_length = 200)
    uploaded_file = PrivateFileField("file", upload_to = 'uploads')
    
class CountedDownloads(models.Model):
    description = models.CharField("description", max_length = 200)
    downloadable = PrivateFileField("file", upload_to = 'downloadables')
    downloads = models.PositiveIntegerField("downloads total", default = 0)
    
def handle_pre_download(instance, field_name, request, **kwargs):
    instance.downloads += 1
    instance.save()
    
pre_download.connect(handle_pre_download, sender = CountedDownloads)