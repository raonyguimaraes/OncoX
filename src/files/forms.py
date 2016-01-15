from django.forms import ModelForm
from files.models import File

# Create the form class.
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']