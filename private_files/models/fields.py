from django.db.models.fields.files import FileField, ImageField

class ProtectedFileField(FileField):
    """
    A subclass of FileField that adds control
    over who can download the file.
    """

    pass


class ProtectedImageField(ImageField):
    """
    A subclass of ImageField that adds control
    over who can download the file.
    """

    pass

