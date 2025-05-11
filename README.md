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

```
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
```

Now to Run our django we need to write the command -
python manage.py runserver port-number

### Django Models

In Django we describe data we need for our application.
Django then uses these models to setup and configure our database to store our data effectively
Django handles the relationship between our models and database

Documentation for Models - https://docs.djangoproject.com/en/1.11/topics/db/models/

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

These are use to override AbstractBaseUser class which is an inbuilt model class in django

Models.py

```
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Managers for User Profile"""
    """Can Manipulate objects and return that object"""

    def create_user(self, name,email, password=None):
        if not email:
            raise ValueError('User Must have an email address')

        if not name:
            raise ValueError("User must enetr a user name")

        if not password:
            raise ValueError('User must enter a password')

        email = self.normalize_email(email=email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self,name,email,password=None):
        """Creating super user"""

        user = self.create_user(name=name,email=email,password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # we need to specify the user field to the unique field of our preference
    # This is because we are overriding the default USERNAME Field which is normally called user name
    # Because we need to use email and password instead of username and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Additional Required Fields apart from email and password

    def get_full_user_name(self):
        """Retrieve User Name"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name.lower()

    # convert a user profile object to a string in python
    def __str__(self):
        return self.email
```

Then you need to add the above UserProfile in the settings.py so that our project should take custom user model instead of in-built user model
settings.py

```
AUTH_USER_MODEL = 'profiles_api.UserProfile'
```

Now we need add new migrations if we are doing any changes in our models
Migration file contains the steps required to modify our database to match our updated models

To add new migrations, cli command is

```
python manage.py makemigrations
```

To run all the migrations, cli command is

```
python manage.py migrate
```

Django Admin - https://docs.djangoproject.com/en/1.11/ref/contrib/admin/

CLI Command to Create a super user :

```
python manage.py createsuperuser
```

To Enable Django Models, we use admin.py file in our project

```
from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)
```

Django Admin override models - https://docs.djangoproject.com/en/2.2/ref/models/options/#verbose-name

Now run the server and go to the url - port-number/admin

### Django Rest Framework

There are two types of views in Djano Rest Framework

- Api-View
- Viewset

#### Api-View -

- Describe logic to make API end points
- Allows us to define functions which matches http request
- Perfect for implementing complex logics
- Calling other APIs
- Working with local files
- Officail documentation - https://www.django-rest-framework.org/api-guide/views/

views.py - Write your end point logic

```
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of ApiView features """
        an_apiview = [
            "Uses Http methods as functions (get,put,post,patch, delete)"
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped mannualy to URLs"
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
```

URL Dispatcher - https://docs.djangoproject.com/en/1.11/topics/http/urls/

path function official doc - https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.path

Include url docs - https://docs.djangoproject.com/en/2.2/ref/urls/#django.urls.include

Now create a new urls.py in your app

```
from django.urls import path
from profiles_api import views

urlpatterns = [
   path('hello-view/',views.HelloApiView.as_view())
]
```

Now go to urls.py and add your end points

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('profiles_api.urls')) # profiles_api.urls = app.urls
]
```

#### Serializers

Serializer is a feature in django rest framework that allows you to easily convert data into python objects and vice versa.

Official Docs -

- Serializers - https://www.django-rest-framework.org/api-guide/serializers/
- Serializers Fields - https://www.django-rest-framework.org/api-guide/fields/
- Status Codes - https://www.django-rest-framework.org/api-guide/status-codes/

Create a file serializers.py in your app

```
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    """Serializers also take care of Validations"""
    name = serializers.CharField(max_length=10)
```

Now add serializers in our views.py for post request

```
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status # For status Codes
from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of ApiView features """
        an_apiview = [
            "Uses Http methods as functions (get,put,post,patch, delete)"
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped mannualy to URLs"
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create the Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})

```

### Viewset

So what are view sets? Just like API views, view sets allow

us to write the logic for our endpoints however instead of defining functions

which map to HTTP methods view sets accept functions that map to common API

object actions such as list for getting a list of objects

Create for creating

new objects retrieve for getting a specific object update for updating an

object partial update for updating part of an object and finally destroy for

deleting an object

Additionally view sets can take care a

lot of the common logic for us they're perfect for writing apis that perform

standard database operations and they're the fastest way to make an api which

interfaces with a database back-end

So when should you use view sets? Well a lot

of the time this comes down to personal preference however here are some

examples of cases when you might want to prefer a view set over an API view for

example if you need to write an API that performs a simple create read update and

delete operation on an existing database model

or you need a quick and simple API

to manage predefined objects or maybe you need a very basic custom logic

additional to the view set features already provided by the Django rest

framework

we'll learn more about that one in a bit finally you might want to

use a view set if your API is working with

standard database structure that's a basic overview of the view set don't

worry if you don't fully understand it at this point

sometimes you need to see an action for it to make sense so in the following

lessons in this section I'm going to walk you through creating a very basic

```
from rest_framework import viewsets
...
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        ...

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
```

Update app/urls.py

```
from django.urls import path,include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
```

### Building APIs for profiles_api

Model Serializer docs - https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

### UPDATE: Bug in profile serializer

Update: I've inserted this page because a fellow student pointed out there is a bug in the UserProfileSerializer (thanks Avi!)

(This is a temporary insert until we can update the videos appropriately)

Issue

If a user updates their profile, the password field is stored in cleartext, and they are unable to login.

Cause

This is because we need to override the default behaviour of Django REST Frameworks ModelSerializer to hash the users password when updating.

Fix

To fix the issue, add the below method to the UserProfileSerializer

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

The final serializers.py file will look like this: https://github.com/LondonAppDev/profiles-rest-api/blob/master/profiles_api/serializers.py#L34

Explanation

The default update logic for the Django REST Framework (DRF) ModelSerializer code will take whatever fields are provided (in our case: email, name, password) and pass them directly to the model.

This is fine for the email and name fields, however the password field requires some additional logic to hash the password before saving the update.

Therefore, we override the Django REST Framework's update() method to add this logic to check for the presence password in the validated_data which is passed from DRF when updating an object.

If the field exists, we will "pop" (which means assign the value and remove from the dictionary) the password from the validated data and set it using set_password() (which saves the password as a hash).

Once that's done, we use super().update() to pass the values to the existing DRF update() method, to handle updating the remaining fields.

serializers.py

```
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    """Serializers also take care of Validations"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','name','email','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }

    # Overriding the default create method of serializers.ModelSerializer

    def create(self,validated_data):
        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
```

views.py

```
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status # For status Codes
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of ApiView features """
        an_apiview = [
            "Uses Http methods as functions (get,put,post,patch, delete)"
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped mannualy to URLs"
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create the Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
```

### Authentication And Autorizations

noticed there is one issue with this API and that is that any user can

anonymously make changes to any other user's profile so you can head over to

the profile with ID 2 and you can change the name change the password or

change any of the details with this API without being authenticated and you can

do the same to user profile 1 now this obviously would not work for a real API

we want to be able to restrict the users so they can only make changes to their

##### permissions.py

Official Documentation - https://www.django-rest-framework.org/api-guide/permissions/

Add permissions.py file in our app

```
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile or not"""

        if request.method in permissions.SAFE_METHOD:
            return True

        return obj.id == request.user.id

```

###### Authentication

Now add Authentication in your views.py file

```
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status # For status Codes
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from profiles_api import models

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of ApiView features """
        an_apiview = [
            "Uses Http methods as functions (get,put,post,patch, delete)"
            "Is similar to a traditional Django View",
            "Gives you the most control over application logic",
            "Is mapped mannualy to URLs"
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create the Hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile)

```

How to add Filters -

```
from rest_framework import filters

...

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    ...
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

```

filter_backends = (filters.SearchFilter,) => adding filters
search_fields = ('name', 'email',) => adding fields by which we would search

### Creating Login API

views.py file

```
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
```

urls.py

```
from django.urls import path,include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
```

##### Setting Token Header using Mode Header Extension

After creating the token, pass that token in the mod Header extension under Request Headers
Under Name section write Authorization
Under Value section write the Token {token}

### Creating profile feed model

models.py

```
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from profiles_project import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Managers for User Profile"""
    """Can Manipulate objects and return that object"""

    def create_user(self, name,email, password=None):
        if not email:
            raise ValueError('User Must have an email address')

        if not name:
            raise ValueError("User must enetr a user name")

        if not password:
            raise ValueError('User must enter a password')

        email = self.normalize_email(email=email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self,name,email,password=None):
        """Creating super user"""

        user = self.create_user(name=name,email=email,password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # we need to specify the user field to the unique field of our preference
    # This is because we are overriding the default USERNAME Field which is normally called user name
    # Because we need to use email and password instead of username and password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Additional Required Fields apart from email and password

    def get_full_user_name(self):
        """Retrieve User Name"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of User"""
        return self.name.lower()

    # convert a user profile object to a string in python
    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text

```

Now write commands on cmd

```
python manage.py makemigrations
python manage.py migrate
```

admin.py

```
from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
```

serializers.py

```
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

```

permissions.py

```
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile or not"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
```

views.py

```
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
```

Django Documentation - https://docs.djangoproject.com/en/1.11/
DRF(Django Rest Framework Documentation) - https://www.django-rest-framework.org/
