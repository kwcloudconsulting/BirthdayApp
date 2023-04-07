from django import forms
from .models import BirthdayMessage

class BirthdayMessageForm(forms.ModelForm):
    class Meta:
        model = BirthdayMessage
        fields = ['message']
