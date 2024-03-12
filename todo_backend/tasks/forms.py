# forms.py

from django import forms
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = '__all__'  # Điều này sẽ bao gồm tất cả các field trong model