from django.shortcuts import render
from .forms import FileForm
from django.core import serializers
import json
from .models import CarModel

def handleFile(f):
	with open('tempData.json', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def getCar(model, year):
	carData = CarModel.objects.filter(model=model, model_year=year).values()
	return carData

def updateCar(car,instance):
	car.update(model_year=instance['model_year'])
	car.update(make=instance['make'])
	car.update(model=instance['model'])
	car.update(rejection_percentage=instance['rejection_percentage'])
	car.update(reason_1=instance['reason_1'])
	car.update(reason_2=instance['reason_2'])
	car.update(reason_3=instance['reason_3'])
	return


def index(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			file = json.loads(request.FILES['file'].read())
			for instance in file:
				checkCar = getCar(instance['model'], instance['model_year'])
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
	# allData = CarModel.objects.all()
	# allData.delete()
	return render(request, 'index.html', {'form': form, 'fileJs': fileJs})
