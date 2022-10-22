from cProfile import label
from django import forms
from django.forms import ModelForm
from .models import File

class FileForm(ModelForm):
	class Meta:
		model = File
		fields = ["file",]
		labels = {
			"file": ""
		}
		widgets = {
			'file': forms.FileInput(attrs={'class': 'upload'}),
		}
