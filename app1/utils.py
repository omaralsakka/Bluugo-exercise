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