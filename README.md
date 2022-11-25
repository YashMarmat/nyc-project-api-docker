# nyc-project-api-docker

# Table of contents
- [Tech_stack_involved](#Tech_stack_involved)
- [About_this_API](#About_this_API)
  * [List_of_Trips](#List_of_Trips)
  * [Single_Trip_Instance](#Single_Trip_Instance)
- [Project_Installation](#Project_Installation)
  * [Docker](#Docker)


## Tech_stack_involved
- Python
- Django
- Django Rest Framework
- Sqlite database
- Docker

## About_this_API
Django application that serves a web service API for bicycle trip information in New York City. 
Provides following informations;
- list_of_trips
- weather_conditions
- observation_stations 
- nearest_station
- weather_for_the_trip_start_time

### List_of_Trips

<b>GET</b> `http://127.0.0.1:8000/api/v1/`

This api displays all the users trip with pagination (2 results per page), the "count" object (provided django rest framework) tells total number of objects 
present in this api request (for demo i have just taken 5 entries from the csv but you can enter more, more on this shortly). The "next" and "previous" objects 
contain links of the next and previous endpoints (here we basically showing the whole list of results through multiple pages, 2 objects per page). 

<p align="center">
<img width="429" alt="image" src="https://user-images.githubusercontent.com/59337853/203978735-81241242-8fba-4e98-aaf3-f0bf5882d923.png">
</p>

### Single_Trip_Instance
<b>GET</b> `http://127.0.0.1:8000/api/v1/33723`

This api contains all the trip details of a single user, containing weather details, stations information, nearest station and trip start weather information
, as shown below;
<p align="center">
  <img width="293" alt="image" src="https://user-images.githubusercontent.com/59337853/203980502-b8800566-d1b8-414d-a81e-4eb8c98fc5ff.png">
</p>

## Project_Installation
after downloading/cloning the repository code, follow below steps:

### Docker

- Run docker
`sudo dockerd` (keep it running in a seperate terminal) 

- Clone the Repository
`git clone https://github.com/YashMarmat/nyc-project-api-docker.git`

- Cd into directory
`cd nyc-project-api-docker/`

- Start docker container
`sudo docker-compose up`

- visit the django rest api page (or you can use postman)

`http://127.0.0.1:8000/api/v1/` (list of ride)

`http://127.0.0.1:8000/api/v1/<id>` (single ride, do mention the object id)

- <b>Test other csv data</b>

- <b>Step 1</b> (open a new terminal window and use the following command, do not close any previous terminal)

* for clearing previous model objects i have created a custom django admin command "emptyridemodel"

`sudo docker-compose exec web python manage.py emptyridemodel`

- <b>Step 2</b> (you can use any current format csv file from here https://s3.amazonaws.com/tripdata/index.html, 
just download the csv and place it at project root level)

* i have created a custom django admin command "customcsvextract" to build model objects (extracts data form csv, requires csv path).

`sudo docker-compose exec web python manage.py customcsvextract ./dummy_csv_data.csv`

- (or you can use this file => JC-202210-citibike-tripdata.csv, contains 80,000 + entries, but it can take very
long time)

- Lastly, once done with the project, you can close the docker container
`sudo docker-compose down`

## All set :)

<p><a href="#top">Back to Top</a></p>

