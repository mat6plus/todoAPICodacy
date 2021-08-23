
# todoAPICodacy
A simple Django Rest Framework todo CRUD API. To run this simple todo API, clone the git repository into your folder of choice and in your terminal preferably a virtual environment but depending on user's preference. 

To run the API ```with assumption docker and docker compose is installed on user's workstation``` first create a directory where you want the app to stay and then a virtual environment using the command ```virtualenv {name of your environment}```. NB: You should have installed the ```Virtualenv using pip install virtualenv``` or other package manager as neccessary. To activate the created virtual environment from the terminal run the following command;
```source {name of virtualenv}/bin/activate``` and if everything was installed correctly you should have a prompt displaying your virtual environment.

Next, clone the repository into the folder created above and have that opened in your favorite editor to visualize the codes, for me I use VS Code and running the command ```code .``` inside the directory housing the cloned repo my editor is up displaying as expected.

From the terminal inside the app directory, run ```pip install -r requirements.txt``` file to download all the dependencies of the project. This project uses postgresql database and as such, it is expected that a user with necessary permissions is to be created along with a database to be used by the application ```in my case the database is named codacy and user: matthew but can leave it as postgres as the user and postgres as database``` granting the user full right over the DB. In the file name ```.env``` which I have excluded from my ```.gitignore file```, adjust all parameters where applicable so that the application is able to connect to the database successfully.
 
When all that is done, to get the app running from the terminal first run the ```docker-compose up to build the image and get the app running``` based on the definition specified in the ```docker-compose.yml file```. Run the following command ```python manage.py migrate and then python manage.py makemigrations``` or ```docker-compose run web python manage.py migrate and then docker-compose run web python manage.py migrate``` to push all migrations such as data models of the app into the databse for the first time or when the data model is adjusted for any reason. ```NB: if the created database and user is properly configured there shouldn't be any error during the migration and also it should also be noted that the migrations commands can be defined within the docker compose file```.

To test the API, you can either run the following command in the terminal ```python manage.py runserver``` or allow it automatically start when the ```docker-compose up``` command is executed after migrations has is successful and the server should be up and running on the default port ```127.0.0.1:8000``` by default with docker-compose the application will run on ```0.0.0.0:8000``` and you can decide to change the port you want to run the app example ```python manage.py runserver 8009 or docker-compose run web python manage.py runserver 8009``` and it will run on that port and all corresponding endpoints should work as expected. 

The API should be accessible from the url ```127.0.0.1:8000/api or 127.0.0.1:{defined_port_number}/api or 0.0.0.0:8000/api with docker-compose running```. NB: By default there wouldn't be any user within the system and as such to create a user, run this command ```python manage.py createsuperuser or docker-compose run python manage.py createsuperuser``` from the terminal and you should be prompted to enter desired username, email and password.

Other users can be created from the Django Admin panel which is accessible from ```127.0.0.1:8000/admin or 0.0.0.0:8000/admin``` and you should be presented with a login which the above created super user credentials can be used to login and from the users tile on the admin interface other user's can be created or from the django shell.

The Following are the endpoints and can be accessible from both the terminal using CURL or from the browser by pointing to the following endpoints;

```127.0.0.1:8000/api or 0.0.0.0:8000/api with docker-compose ---- List all todo object
127.0.0.1:8000/api/create or 0.0.0.0:8000/api/create with docker compose --- To create a todo onject
127.0.0.1:8000/api/detail/1 or 0.0.0.0:8000/api/detail/1 with docker compose ---- To get todo by ID and in this case id:1
127.0.0.1:8000/api/update/1 or 0.0.0.0:8000/api/update/1 with docker compose ---- To update the todo object in this case id:1
127.0.0.1:8000/api/delete/1 or 0.0.0.0:8000/api/delete/1 with docker compose---- To delete the todo object in this case id:1
```

#NB: Incase where the API is not rendering well in the browser like the css and js files not loading, rather than using the ```python manage.py runserver``` command only, kindly add the --insecure to it like so ```python manage.py runserver --insecure``` same applicable while using the docker compose.

Bellow is the ```127.0.0.1:8000/api``` screenshot same as when it's running on ```0.0.0.0:8000/api```

![api](https://user-images.githubusercontent.com/19800135/130051743-d16c8722-e558-44aa-afa1-e4619c83978f.png)
![todo Create](https://user-images.githubusercontent.com/19800135/130327811-817f6641-b7c9-47ed-a885-d4b1260bc778.png)
![todo Update](https://user-images.githubusercontent.com/19800135/130327823-229b4804-d78d-44d2-b57a-f471af3dd886.png)
![todo Delete](https://user-images.githubusercontent.com/19800135/130327828-374b450e-acb8-402b-b081-da843e749a00.png)




Thank you

Matthew Johnson



