from django import forms
from .models import Person
class surveyform(forms.ModelForm):
    class Meta:
        model = Person
        fields='__all__'
