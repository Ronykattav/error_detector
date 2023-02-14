from django.forms import ModelForm
from django import forms
from .models import UserInput


class UploadForm(forms.ModelForm):
    # userId = forms.IntegerField()
    # problem = forms.TextInput()
    # serialNum = forms.TextInput()
    # msg = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = UserInput
        fields = ['userId', 'problem', 'serialNum', 'onLights', 'offLights', 'blinkingLights']
