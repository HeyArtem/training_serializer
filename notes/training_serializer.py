training_serializer

% mkdir training_serializer
% cd training_serializer
% python3 -m venv venv
% source venv/bin/activate
% pip install -U pip
% pip install -U setuptools
	pip install -U pip && pip install -U setuptools

	Если хочется ещё короче, то можно всё в одной команде:
	pip install -U pip openpyxl pandas
% brew update # Обновляет информацию о доступных пакетах
% brew upgrade	# Обновляет установленные пакеты
% brew cleanup	# Удаляет старые версии пакетов

% pip install django==4.2.1
% django-admin startproject training_serializer .  ( 💠Точка (.) в конце говорит Django, что не надо создавать лишнюю вложенную папку!)    

python manage.py runserver
python manage.py startapp myapi 

	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'myapi.apps.MyapiConfig',
	]
	
python manage.py migrate
python manage.py createsuperuser

	Username (leave blank to use 'heyartem'):art 
	Email address: 
	Password: 0000
	Password (again): 0000
	
python manage.py runserver

myapi/models.py
	from django.db import models
	
	class Hero (models.Model):
	    name = models.CharField(max_length=60)
	    alias = models.CharField(max_length=60)
	
	    def __str__(self):
	        return self.name
	    
	
python manage.py makemigrations
python manage.py migrate


myapi/admin.py
	from django.contrib import admin
	from .models import Hero
	
	admin.site.register(Hero)

Заполнил БД

pip install djangorestframework

	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'myapi.apps.MyapiConfig',
	    'rest_framework',
	
	]
	
! myapi/serializers.py

myapi/serializers.py
	from rest_framework import serializers
	from .models import Hero
	
	class HeroSerializer(serializers.HyperlinkedModelSerializer):
	    class Meta:
	        model = Hero
	        fields = (
	            'name',
	            'alias'
	        )
	        
myapi/views.py
	from django.shortcuts import render
	from rest_framework import viewsets
	from .serializers import HeroSerializer
	from .models import Hero
	
	class HeroViewSet(viewsets.ModelViewSet):
	    '''
	    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework. 
	    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
	    На практике оно не очень!
	    '''
	    queryset = Hero.objects.all().order_by('name')
	    serializer_class = HeroSerializer

training_serializer/urls.py
	from django.contrib import admin
	from django.urls import path, include
	
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('myapi.urls')),
	]

! myapi/urls.py
myapi/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]


python manage.py runserver

	http://127.0.0.1:8000/
	
			HTTP 200 OK
			Allow: GET, HEAD, OPTIONS
			Content-Type: application/json
			Vary: Accept
			
			{
			    "heroes": "http://127.0.0.1:8000/heroes/"
			}
			

	http://127.0.0.1:8000/heroes/
		HTTP 200 OK
		Allow: GET, POST, HEAD, OPTIONS
		Content-Type: application/json
		Vary: Accept
		
		[
		    {
		        "name": "Дэдпул",
		        "alias": "Болтливый наемник"
		    },
		    {
		        "name": "Росома́ха",
		        "alias": "Ло́ган"
		    }
		]
		
	
	http://127.0.0.1:8000/heroes/1/
		HTTP 200 OK
		Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
		Content-Type: application/json
		Vary: Accept
		
		{
		    "id": 1,
		    "name": "Дэдпул",
		    "alias": "Болтливый наемник"
		}

добавить нового
http://127.0.0.1:8000/heroes/ (в post-form)
	Captain America
	Первый Мститель, Суперсолдат
	
	HTTP 200 OK
	Allow: GET, POST, HEAD, OPTIONS
	Content-Type: application/json
	Vary: Accept
	
	[
	    {
	        "id": 5,
	        "name": "Captain America",
	        "alias": "Первый Мститель, Суперсолдат"
	    },
	    {
	        "id": 3,
	        "name": "XXX",
	        "alias": "xxx"
	    },
	    {
	        "id": 4,
	        "name": "XXX",
	        "alias": "xxx"
	    },
	    {
	        "id": 1,
	        "name": "Дэдпул",
	        "alias": "Болтливый наемник"
	    },
	    {
	        "id": 2,
	        "name": "Росома́ха",
	        "alias": "Ло́ган"
	    }
	]



pip install pre-commit
❗️.pre-commit-config.yaml
	repos:
	  - repo: https://github.com/pre-commit/pre-commit-hooks
	    rev: v4.4.0
	    hooks:
	      - id: trailing-whitespace
	      - id: end-of-file-fixer
	      - id: check-yaml
	      - id: check-json
	
	  - repo: https://github.com/psf/black
	    rev: 23.9.1
	    hooks:
	      - id: black
	        require_serial: true
	
	  - repo: https://github.com/pre-commit/mirrors-isort
	    rev: v5.10.1
	    hooks:
	      - id: isort
	        args: [ "--profile", "black" ]
	
	  - repo: https://github.com/PyCQA/flake8
	    rev: 6.1.0
	    hooks:
	      - id: flake8
	        args: [--max-line-length=200]
	        exclude: |
	          (?x)(
	              ^models_app/admin/__init__.py|
	              ^models_app/models/__init__.py|
	              ^models_app/migrations/
	          )
	
	
	  - repo: https://github.com/asottile/pyupgrade
	    rev: v3.11.0
	    hooks:
	      - id: pyupgrade
	
	
	
	#trailing-whitespace
	#  проверки конечных пробелов
	
	#end-of-file-fixer
	#  Следит за тем, чтобы файлы заканчивались новой строкой и только новой строкой.
	
	#check-yaml
	#  Пытается загрузить все файлы YAML для проверки синтаксиса.
	
	#check-json
	#  Пытается загрузить все файлы JSON для проверки синтаксиса.
	
	#black
	#  единый стиль кода, форматирование, единообразие
	
	#isort
	#  для сортировки импорта в алфавитном порядке и автоматического разделения на разделы и по типу.
	
	#pyupgrade
	#  для автоматического обновления синтаксиса для новых версий языка.



❗️-Настраиваю debuger
        Current File-Edit Configuration-+-Python-Name('Debuger')-Script path(путь до manage.py)-
                Parameters(runserver)-Apply OK


❗️.gitignore
	
	
	

pip freeze > requirements.txt

* * * * Показать структуру проекта в графическом виде: * * * *	
	brew install tree  # для macOS 	# Если tree не установлен, сначала установи его:
	tree	# вывести дерево папок:
	tree -L 2	# показать только 2-3 уровня вложенности:
	tree > structure.txt
* * * * * * * * * * * * * * * *


git init
git add . 
git status
git commit -m "initial"







	





