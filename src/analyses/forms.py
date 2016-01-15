from django.forms import ModelForm
from analyses.models import Analysis

# Create the form class.
class AnalysisForm(ModelForm):
    class Meta:
        model = Analysis
        fields = ['name', 'type', 'files']