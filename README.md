# DjangoTutorials

Cheat Sheet - https://drive.google.com/file/d/0B9ZdsGRs88lDUUR4dTM3V2dtMDQ/view?resourcekey=0-RuWILWS9KuWAM3UFi_Laow

Full Source Code - https://github.com/LondonAppDev/profiles-rest-api

How to ask question in StackOverflow - https://londonappdeveloper.com/how-to-ask-questions-on-stack-overflow-and-get-answers/

Api Source Code - https://github.com/LondonAppDev/profiles-rest-api

## Vagrant

Vagrant Allows us to describe what kind of server we need for our app.
We can then save the config as a vagrant file, which allows us to reproduce and share the same server with other developers.
After this it will use Virtual Machines to create virtual servers exactly as we described.
This means our requirements have been installed and running on a virtual server completely in an isolated environment.

### Advantages

- Easy to share the server with others
- Exact the same version of all requirements
- Run exactly the same software as a real production server
- Easily create and destroy the server as needed

## Vagrant vs Docker

| Docker                            | Vagrant                                     |
| --------------------------------- | ------------------------------------------- |
| Open Source Containerization tool | Manage Virtual Development Environments     |
| run app in light weight images    | No out-of-the-box virtualization technology |

Vagrant are easier to learn than docker.

### Installations

- Vagrant - https://github.com/LondonAppDev/profiles-rest-api
- Cheat Sheet - https://github.com/LondonAppDev/build-a-backend-api-python-drf-beginner-cheat-sheet/blob/master/README.md
- Git - https://git-scm.com/
- Virtual Box - https://www.virtualbox.org/wiki/Download_Old_Builds_6_1
- Mod Headers - https://chromewebstore.google.com/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en
- Atom Editor - https://github.blog/news-insights/product-news/sunsetting-atom/

## Setting up your projects

- Github Cheat Sheet - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- Git Commands - https://github.com/LondonAppDev/build-a-backend-api-python-drf-beginner-cheat-sheet/blob/master/README.md
- .gitignore file - https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff
- LICENSE - https://choosealicense.com/licenses/mit/

## Creating a Development Sever

Vagrant allows you define the type of server you need for the project as Vagrant file.

- To create a Vagrant file, command - vagrant init ubuntu/bionic64, here ubuntu/bionic64 is the image container of OS - ubuntu

- It gives a template of vagrant file with ubuntu as VM server
- Vagrant file Example - https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682
- Vagrant up - Download the base image that we have specified in our Vagrant files and it will use Virtual Box to create a new VM and then run our provisioning scripts when it starts the machine
- After this we can connect to Vagrant Server using Vagrant SSH command.
- Command - vagrant ssh

## Python and Django Tutorial

First install python from the official page

To create a new environment we can write - python -m venv {file-path}/{environment-name}
If you want to use Virtual Environments then you need to activate it and to stop it you need de activate it

Commands

- source {path-to-activate-file-of-the-environment}, eg - source /env/bin/activate
- Virtual Environment Cheat Sheet - https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/

Then make a requirements.txt file which consist all the dependencies with their versions
To get the latest versions - https://pypi.org/ (search here the packages)
Now add django and django rest framework with latest versions
Then enter the command - pip install -r requirements.txt to install every dependencies

### Django

To create a django project write the command

To Create a new project - django-admin startproject project-name

To Create a new app

- first navigate your terminal to your desired project
- Then use the command python manage.py startapp app-name

Then enable our app & dependencies in the project's settings.py file under INSTALLED_APPS

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rest_framework', # django rest framework
'rest_framework.authtoken', # Auth Token
'profiles_api' # App Name
]

Now to Run our django we need to write the command -
python manage.py runserver port-number
