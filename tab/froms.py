
from django import forms
from .models import Document

class DocumentsForms(forms.ModelForm):
    class Meta:
        model=Document
        fields=('document',)