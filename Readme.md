# Pet Diary

## About This Project
We utilize Django as our web server, MariaDB as our database, employ Gunicorn to serve our Django application, and leverage Nginx as our reverse proxy.

## Run Yourself
First clone this repository: 
```
git clone https://github.com/james61124/Pet-Daily
cd Pet-Daily
```

### Prerequisites
1. Install Docker -> run docker-install.sh
2. Configure your own `app.env`

   
### Build the service
```
cd Pet-Daily
sudo docker compose --env-file app.env up -d
```

Connect into the container

```
sudo docker exec -it <container_name> /bin/bash
```

Stop all the containers

```
sudo docker compose --env-file app.env down
```

View the status of the containers

```
sudo docker compose --env-file app.env ps
```

View the logs of containers

```
sudo docker compose logs <container_name>
```
```
sudo docker compose inspect <container_name>
```

View all the containers

```
sudo docker container list
```

View all the images

```
sudo docker images
```

Remove the image

```
sudo docker rmi <image_name>
```

# About the service
1. Ensure that port 3306 for mariadb, 8000 for Django server, 81 for Nginx are not used by other process, or you should modify the env file and the settings within them
2. Port 3306 for mariadb cannot be modified
3. mariadb/schema.sql is the sql file which build the database when you start the container, however, in Django file, you should still modify models.py and migrate database to Django project
4. nginx/conf.d/default.conf is the port forward rules for nginx
5. home-python/multimedia is your Django project
6. There will be 5 containers after you build the service, except for go-server, you should connect into the container and modify code inside it
7. Everytime you modify docker-compose.yml, remove the images before you build the service
8. Dockerfile is for python-server, Dockerfile2 is for go-server

# Develope Steps
1. Connect to python-server, you will see a Django project in /home/multimedia
2. Run the server by ```python3 manage.py runserver```, however, if you aim to run the server in an production mode, uncomment ```CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "multimedia.wsgi:application"]``` in Dockerfile, the server will be ran as demon utilizing Gunicorn
3. Once you change the database, Run
```
python3 manage.py makemigrations
python3 manage.py migrate
```
4. you can modify the database in home-python/multimedia/journal/models.py
5. you can add routing rules in home-python/multimedia/multimedia/urls.py
6. you can uncomment log settings in home-python/multimedia/multimedia/settings.py to see the log when you run your server utilizing Gunicorn
7. you can write your code in home-python/multimedia/journal/views.py

# About Testing your server
1. Once the server is running, there's some example request in request/, modify the host or port make sure the request go through nginx



