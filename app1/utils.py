from pickle import FALSE
from .models import CarModel

def getCar(make, model, year):
	carData = CarModel.objects.filter(make=make, model=model, model_year=year).values()
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

def validateInputs(instance):
	if 'model_year' not in instance:
		return False
	elif 'make' not in instance:
		return False
	elif 'model' not in instance:
		return False
	elif 'rejection_percentage' not in instance:
		return False
	elif 'reason_1' not in instance:
		return False
	elif 'reason_2' not in instance:
		return False
	elif 'reason_3' not in instance:
		return False
	else:
		return True
