from django.shortcuts import render
from .forms import FileForm
from django.core import serializers
import json
from .models import CarModel
from .utils import getCar, updateCar, validateInputs

def index(request):

	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			file = json.loads(request.FILES['file'].read())
			for instance in file:
				if validateInputs(instance):
					checkCar = getCar(instance['make'], instance['model'], instance['model_year'])
					if checkCar:
						updateCar(checkCar, instance)
					else:
						newData = CarModel(
							model_year=instance['model_year'],
							make=instance['make'],
							model=instance['model'],
							rejection_percentage=instance['rejection_percentage'],
							reason_1=instance['reason_1'],
							reason_2=instance['reason_2'],
							reason_3=instance['reason_3'])
						newData.save()
	else:
		form = FileForm()
	fileJs = serializers.serialize("python", CarModel.objects.all())
	return render(request, 'index.html', {'form': form, 'fileJs': fileJs})