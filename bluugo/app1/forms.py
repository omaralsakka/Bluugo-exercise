from django import forms
from django.db import models
from django.forms import ModelForm
from .models import File

class FileForm(ModelForm):
	class Meta:
		model = File
		fields = ["file",]
