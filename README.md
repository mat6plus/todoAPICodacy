# todoAPICodacy
A simple Django Rest Framework todo CRUD API. To run this simple todo API, clone the git repository into your folder of choice and in your terminal preferably a virtual environment but depending on user's preference. 

To run the API first create a directory where you want the app to stay and then a virtual environment using the command "virtualenv {name of your environment} and this will create a name for your virtual environment and stated above. NB: You should have installed the "Virtualenv using pip install virtualenv or other package manager as neccessary. To activate the created virtual environment from the terminal run the following command;
```source {name of virtualenv}/bin/activate``` and if everything was installed correctly you should have a prompt displaying your virtual environment.

Next, clone the repository into the folder and have that opened in your favorite editor, for me I use VS Code and running the command (code . ) inside the directory housing the cloned repo. 

From the terminal inside the app directory, run ```pip install -r requirements.txt``` file to download all the dependencies of the project. This project uses postgresql and as such a user with necessary is to be created along with a database granting the user full right over the DB. In the file name .env, adjust all applicable parameters so that the application is able to connect to the database successfully.
 
When all that is done, to get the app running from the terminal run this command ```python manage.py makemigrations``` or ```docker-compose run web python manage.py migrate``` to push all migrations such as data models of the app into the DB. NB: if the created DB and user is properly configured there shouldn't be any error during the migration;

To test the API, run the following command in the terminal ```python manage.py runserver``` or automatically started when the ```docker-compose up``` command is executed and the server should be up and running on the default port ```127.0.0.1:8000```. The API should be accessible from the url ```127.0.0.1:8000/api```. NB: By default there wouldn't be any user within the system and as such to create a user, run this command ```python manage.py createsuperuser``` and you should be prompted with to enter desired username, email and password.

Other users can be created from the Django Admin panel which is accessible from ```127.0.0.1:8000/admin``` and you should be presented with a login which the above created credentials can be used to login and from the users tile on the admin interface new user's can be created same also can be done from the terminal but from the django shell using ```docker-compose exec web python manage.py createsuperuser```. 

The Following are the endpoints and can be accessible from both the terminal using CURL or from the browser by pointing to the following endpoints;

```127.0.0.1:8000/api  ---- List all todo object
127.0.0.1:8000/api/create --- To create a todo onject
127.0.0.1:8000/api/detail/1 ---- To get todo by ID and in this case 1
127.0.0.1:8000/api/update/1 ---- To update the todo object in this case 1
127.0.0.1:8000/api/delete/1 ---- To delete the todo object in this case 1
```





