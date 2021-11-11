# Met office climate app

This is a met office climate app. This app has an endpoint where it retrieves the data from Met Office API, parses it, and stores it in the Django model. It also has an endpoint where it retrieves data from the DB and returns it in a JSON format 

## Folllow the instruction to run it in your local environment

Note: Clone the repository and you should have docker installed in your system to run this app

Below line is to build the image and run the docker container
```
docker-compose up --build
```
Once the docker creates an image from the Dockerfile and runs the container make a POST request to the below endpoint to create/update the data in the DB from the met office API. 

```
POST http://127.0.0.1:8000/weather-api/met-office-climate-data/
```
To view the inserted data in the database then make the GET request to the same endpoint
```
GET http://127.0.0.1:8000/weather-api/met-office-climate-data/
```


# NOTE:
.env file has been ignored before running the docker-compose up --build command please reach out to me to get the .env file.
