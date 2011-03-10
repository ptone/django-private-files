from django.contrib.admin import site, ModelAdmin
from testproject.testapp.models import FileSubmission

site.register(FileSubmission, ModelAdmin)