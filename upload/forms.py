from django.forms import ModelForm
from .models import Upload

class MeetingModelForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['description', 'document',]
