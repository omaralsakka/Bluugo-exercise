# Bluugo-exercise

## :diamond_shape_with_a_dot_inside: **Project's goal:**

This project is pre assignment from <a href="https://bluugo.fi/en-us/">Bluugo Oy<a/> is about creating a web page that takes json file with cars data<br/>
then it displays them into a table. Afterwards you can search lively into the data that is saved.<br />
The project had to be written in ```Django```.

## :page_with_curl: **How it's done:** 

- User adds json file from the web page
- The file checked if it's in the correct format
- If the car is data is totally new, a new data saved in ```SQL Light``` <strong>database</strong> 
- If the car exist in the <strong>database</strong>, the car data will be updated only

## :warning: **Prerequisites:**

- ```python3```
- For deployment: ```django_on_heroku``` - ```gunicorn```

## :green_square: Run

- ```git clone ```
- ```cd Bluugo-exercise```
- ```python3 manage.py runserver```

## :heavy_plus_sign: Deployment

The project is ready to deploy on Heroku if needed.
