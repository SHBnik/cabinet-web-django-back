
# Parrot 
# Getting started 
To use parrot web site you should follow bellow instructions.
## 1. Python django server 
This server is using to save users login and their commands.  
our server used django platform to and a rest API to save data in SQL server.

1. Step One : **Installing python3**
>if you have python3 already skip this step

	
 * MacOS :
	>
		brew install python3 
	
* Linux :
	>
		sudo apt-get update
		sudo apt-get install python3.6
2. Step Two : **Installing pip3**
>if you have pip3 already skip this step
* MacOs :
	>
		brew install pip3
* Linux :
	>
		sudo apt-get install python3-pip
	
3. Step Three : **Installing django and dependencies**
	* First we installing django :
		>
			pip3 install django 
	* Because we are using rest API django need it's own framework for django rest which is _django_rest_. we installing it using this :
		>
			pip3 install djangorestframework
			pip3 install markdown 
			pip3 install django-filter
		Notice : markdown and django-filter are ordinary packages and can not be installed
	* We don't have an online server and we run our server on our device so we should install an cross origin sharing resource to use cross-domain request. so we used to install _django-cors-headers_ :
		>
			pip3 install django-cors-headers
4. Step Four : **starting django server**
* First you should copy **"serverSide"** folder somewhere which have not specefic permissions.(Like Desktop/)
* Then go to that repository  and then 
	* If you want to delete old datas from database use this command :
	>
		python3 manage.py flush
	Notice : its necessary for first use.
	* Then you can run your server with this command :
	>
		python3 manage.py runserver

**You runned your server and our website can use this server to store data**

* For seeing Users that logined from website you can see this url on your browser.
	> 
		127.0.0.1:8000/Log/
* For seeing all commands that comes from website you can see this url on your browser.
	> 
		127.0.0.1:8000/Command/
* For seeing commands of a specific user that comes from website you can see this url on your browser.
	> 
		127.0.0.1:8000/Command/<user_id>/
	
	* user id is  id of a specific user
