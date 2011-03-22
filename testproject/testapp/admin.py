from django.contrib.admin import site, ModelAdmin
from testproject.testapp.models import FileSubmission, CountedDownloads


class CountableModelAdmin(ModelAdmin):
    readonly_fields = ("downloads", )

site.register(FileSubmission, ModelAdmin)
site.register(CountedDownloads, CountableModelAdmin)