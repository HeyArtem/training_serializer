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

	from .models import Hero
	from .serializers import HeroSerializer

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
	from django.urls import include, path

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('myapi.urls')),
	]

! myapi/urls.py
myapi/urls.py

from django.urls import include, path
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



🚸 🚸 🚸 🚸 🚸 🚸 🚸 Памятка pre-commit 🚸 🚸 🚸 🚸 🚸 🚸 🚸

pip install pre-commit
pre-commit install		✅ Это настроит автоматический запуск хуков при каждом git commit.

Использование
	git add .
	git commit -m "Test pre-commit" 		✅ Сработает на этом шаге, повторять эти шаги, пока ошибки не исчезнут


		🧠 Полезные команды
	pre-commit install          	-Устанавливает git hook
	pre-commit run              	-Запускает все хуки вручную
	pre-commit run --all-files    	-Прогоняет все файлы через проверки
	pre-commit uninstall        	 -Удаляет git hook
	git commit -m "Твой комментарий к коммиту" --no-verify        	 -Обход pre-commit


.pre-commit-config.yaml (❕добавил в исключение папку notes/)
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
	        exclude: ^notes/

	  - repo: https://github.com/pre-commit/mirrors-isort
	    rev: v5.10.1
	    hooks:
	      - id: isort
	        args: [ "--profile", "black" ]
	        exclude: ^notes/

	  - repo: https://github.com/PyCQA/flake8
	    rev: 6.1.0
	    hooks:
	      - id: flake8
	        args: [--max-line-length=200]
	        exclude:
	          '^notes/|
	          ^models_app/admin/__init__.py|
	          ^models_app/models/__init__.py|
	          ^models_app/migrations/'

	  - repo: https://github.com/asottile/pyupgrade
	    rev: v3.11.0
	    hooks:
	      - id: pyupgrade
	        exclude: ^notes/



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


Можно также игнорировать отдельные файлы:
	exclude: notes/training_serializer.py
	exclude: 'notes/.*\.py'  # Игнорирует все .py в папке notes

		🧠 Объяснение регулярки:
	^notes/ 	-Начинается с notes/→ игнорируем всю папку
	^models_app/admin/__init__.py	 -точный путь к файлу
	^models_app/migrations/	 -вся папка migrations


🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸 🚸





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

🔱  🔱  🔱  🔱  🔱  🔱  🔱 GIT памятка 🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱
✅ 1 запуск
	git init
	git add .
	git status
	git commit -m "initial"
	creat new rep on https://github.com/HeyArtem/
	git branch -M main
	git remote add origin git@github.com:HeyArtem/training_serializer.git
	git push -u origin main
	git status

✅ Добавить сделанные изменения
	Я в нужной ветке!
	git status	 # Не залитые файлы - красные
	git add .
	git commit -m "add README.md"
	git push


✅ Если я работаю на втором компьютере в ветке art_macbook, и хочу
	подтянуть все изменения из github из ветки main
 	(в main я внес изменения из первого-моего стационарного компьютера)
	git checkout main
	git pull origin main
	git checkout art_macbook
	git merge main

исправил конфликты

	git status
	git add .
	git commit -m "Resolved merge conflicts between main and art_macbook"
	git log --oneline       #Убедись, что слияние завершено:
	git push origin art_macbook


однажды я написал
        $ git reset --hard
                и это пиздец! Не делай так Артем!
откат к старой миграции (models_app-приложение с мтграциями, 0003-номер миграции к которой нужно откатиться)
	python manage.py migrate models_app 0003.

✅ Клонирование репозитория с GitHub (HTTPS)
	- создать директорию на компьютере
	- открыть нужный репозиторий-Code-HTTPS-скопировать ссылку
	- $ git clone + ссылка
	- перейти в паку с проектом
	- $ python3 -m venv venv создать виртуальное окружение
	- $ source venv/bin/activate активировать виртуальное окружение
	- $ pip install -U pip setuptools
	- $ pip install -r requirements.txt установить библиотеки из requirements.txt
	- $ code . открыть проект
	- запустить main.py (возможно потребуются свежие header)


🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱  🔱


⌄
⌄
def save(self, *args, **kwargs):
    if not self.alias:
        self.alias = f"У {self.name} еще нет прозвища!"
    super().save(*args, **kwargs)
Это более гибкий способ.


⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕
🛠 ОСНОВНЫЕ ПАРАМЕТРЫ ПОЛЕЙ (Django)		"ASCII-таблица" или "текстовая таблица с рамками"
+---------------+-----------------------------+--------------------------------------------------+
| Параметр      | По умолчанию                | Что делает                                       |
+---------------+-----------------------------+--------------------------------------------------+
| verbose_name  | snake_case (например         | Подпись для людей (в админке, документации)     |
|               | first_name → First name)     |                                                  |
+---------------+-----------------------------+--------------------------------------------------+
| max_length    | Нет                         | Максимальная длина строки (CharField)            |
+---------------+-----------------------------+--------------------------------------------------+
| blank         | False                       | Можно ли оставить поле пустым при               |
|               |                             | в форме / НЕ в БД                                |
+---------------+-----------------------------+--------------------------------------------------+
| null          | False                       | Можно ли хранить в БД значение NULL              |
+---------------+-----------------------------+--------------------------------------------------+
| unique        | False                       | Должно ли значение быть уникальным               |
+---------------+-----------------------------+--------------------------------------------------+
| default       | Нет                         | Значение по умолчанию                            |
+---------------+-----------------------------+--------------------------------------------------+
| auto_now      | Нет                         | Обновляет время каждый раз при сохранении        |
|               |                             | (DateTimeField)                                  |
+---------------+-----------------------------+--------------------------------------------------+
| auto_now_add  | Нет                         | Устанавливает время один раз при создании        |
|               |                             | объекта                                          |
+---------------+-----------------------------+--------------------------------------------------+
| choices       | Нет                         | Список допустимых вариантов значений             |
+---------------+-----------------------------+--------------------------------------------------+
| primary_key   | False                       | Является ли поле первичным ключом                |
+---------------+-----------------------------+--------------------------------------------------+
| editable      | True                        | Можно ли редактировать поле в админке или        |
|               |                             | через форму                                      |
+---------------+-----------------------------+--------------------------------------------------+
| on_delete     | —                           | Что делать с записью, если связанный объект      |
|               |                             | удален (ForeignKey)                              |
+---------------+-----------------------------+--------------------------------------------------+





💥 ВАРИАНТЫ on_delete (для ForeignKey)

+----------------------+-------------------------------------------------------------+
| on_delete=...        | Что происходит                                            |
+----------------------+-------------------------------------------------------------+
| models.CASCADE       | Удаляет текущий объект, если удалён связанный              |
+----------------------+-------------------------------------------------------------+
| models.PROTECT       | Не даёт удалить связанный объект, если есть зависимые      |
|                      | записи                                                    |
+----------------------+-------------------------------------------------------------+
| models.SET_NULL      | Устанавливает NULL, если связанный объект удален          |
|                      | (требует null=True)                                        |
+----------------------+-------------------------------------------------------------+
| models.SET_DEFAULT   | Устанавливает значение по умолчанию, если связанный       |
|                      | объект удален                                             |
+----------------------+-------------------------------------------------------------+
| models.SET(...)      | Устанавливает указанное значение, например: SET(1),       |
|                      | SET(get_default_user)                                      |
+----------------------+-------------------------------------------------------------+
| models.DO_NOTHING    | Ничего не делает (Осторожно! Может сломать целостность     |
|                      | данных)                                                  |
+----------------------+-------------------------------------------------------------+



					+------------------------+-----------------------------+
					| Тип связи              | Поддерживает on_delete?     |
					+------------------------+-----------------------------+
					| ForeignKey             | Да                          |
					+------------------------+-----------------------------+
					| OneToOneField          | Да                          |
					+------------------------+-----------------------------+
					| ManyToManyField        | Нет                         |
					+------------------------+-----------------------------+


⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕ ⭕


Есть проблемы с миграциями потому что у меня уже заполнена база данных а я где-то написал что значение
должно быть уникальными и пустыми не допускается. Сейчас я уберу в моделях уникальность, сделаю миграции,
заполню всё и потом сделай повторный миграции

rm db.sqlite3
удаляю все из папки с миграциями (остаестя только __init__.py)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
		Username (leave blank to use 'heyartem'):art
		Email address:
		Password: 0000
		Password (again): 0000

myapi/models.py
	from django.db import models


	def default_alias(name):
	    ''' callable-функция. Создание дефолтного alias '''
	    return f"У {name} еще нет прозвища!"


	class Hero(models.Model):
	    name = models.CharField(
	        verbose_name='Имя',
	        max_length=60,
	        blank=False,
	        null=False,
	        unique=True
	    )
	    alias = models.CharField(
	        verbose_name='Прозвище',
	        max_length=60,
	        blank=True,
	        null=False,
	        unique=True,
	        default=default_alias
	    )
	    date_of_birth = models.DateField(
	        verbose_name='Дата рождения',
	        blank=False,
	        null=False,
	    )
	    created_at = models.DateTimeField(
	        verbose_name='Дата создания',
	        auto_now_add=True,
	        null=False,
	    )
	    updated_at = models.DateTimeField(
	        verbose_name='Дата обновления',
	        auto_now=True,
	        null=False,
	    )
	    content = models.TextField(
	        verbose_name='Oписание',
	        blank=False,
	        null=False,
	        unique=True
	    )

	    class Meta:
	        verbose_name = "Герой"
	        verbose_name_plural = "Герои"

	    def save(self, *args, **kwargs):
	        ''' Переопределяю т.к создание дефолтного alias'''
	        if not self.alias:
	            self.alias = default_alias(self.name)
	        super().save(*args, **kwargs)

	    def __str__(self):
	        return self.name
Модель выше не смог запустить, проблема: ''' Переопределяю т.к создание дефолтного alias'''

rm db.sqlite3
удаляю все из папки с миграциями (остаестя только __init__.py)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
		Username (leave blank to use 'heyartem'):art
		Email address:
		Password: 0000
		Password (again): 0000

Рабочая модель:
myapi/models.py
	from django.db import models


	class Hero(models.Model):
	    name = models.CharField(
	        verbose_name='Имя',
	        max_length=60,
	        blank=False,
	        null=False,
	        unique=True
	    )

	    alias = models.CharField(
	        verbose_name='Прозвище',
	        max_length=60,
	        blank=False,
	        null=False,
	        unique=True,
	    )
	    date_of_birth = models.DateField(
	        verbose_name='Дата рождения',
	        blank=False,
	        null=False,
	    )
	    created_at = models.DateTimeField(
	        verbose_name='Дата создания',
	        auto_now_add=True,
	        null=False,
	    )
	    updated_at = models.DateTimeField(
	        verbose_name='Дата обновления',
	        auto_now=True,
	        null=False,
	    )
	    content = models.TextField(
	        verbose_name='Oписание',
	        blank=False,
	        null=False,
	        unique=True
	    )

	    class Meta:
	        verbose_name = "Герой"
	        verbose_name_plural = "Герои"

	    def save(self, *args, **kwargs):
	        ''' Переопределяю т.к создание дефолтного alias'''
	        if not self.alias:
	            self.alias = default_alias(self.name)
	        super().save(*args, **kwargs)

	    def __str__(self):
	        return self.name

Теперь пишу ДВА вида СЕРИАЛИЗАЦИИ (
	Вар 1, на APIView
	Вар 2, на Дженериках: ListAPIView

myapi/serializers.py 	(🈯сериалайзер буду использовать один в обоих вариантах)
	from rest_framework import serializers
	from .models import Hero


	class HeroSerializer(serializers.HyperlinkedModelSerializer):
	    class Meta:
	        model = Hero
	        fields = ("id", "name", "alias")


	class ListHeroSerializer(serializers.ModelSerializer):
	    class Meta:
	        model = Hero
	        fields = [
	            'id', 'name', 'alias', 'content', 'date_of_birth', 'created_at', 'updated_at',
	        ]

myapi/urls.py
	from django.urls import include, path
	from rest_framework import routers

	from . import views
	from .views import *

	router = routers.DefaultRouter()
	router.register(r"heroes", views.HeroViewSet)

	urlpatterns = [
	    path("", include(router.urls)),
	    path("api/", include("rest_framework.urls", namespace="rest_framework")),

	    # Hero var 1
	    path("heros/", HeroListAPIView.as_view()),

	    # Hero var 2 (на Дженериках)
	    path("herosV2/", HeroListAPIViewVAR2.as_view()),

	]


myapi/views.py
	from rest_framework import viewsets
	from .models import Hero
	from .serializers import HeroSerializer, ListHeroSerializer
	from rest_framework.views import APIView    # Var 1
	from rest_framework.generics import ListAPIView    # Var 2
	from rest_framework.response import Response
	from rest_framework import status



	class HeroViewSet(viewsets.ModelViewSet):
	    """
	    ModelViewSet - это специальное представление, которое предоставляет Django Rest Framework.
	    Он будет обрабатывать GET и POST для Heroe без дополнительной работы.
	    На практике оно не очень!
	    """

	    queryset = Hero.objects.all().order_by("name")
	    serializer_class = HeroSerializer


	class HeroListAPIView(APIView):
	    """
	    Вар 1, на APIView
	    """

	    def get(self, request, *args, **kwargs):
	        hero = Hero.objects.all().order_by('-id')

	        return Response(
	            ListHeroSerializer(hero, many=True).data,
	            status=status.HTTP_200_OK
	        )

	class HeroListAPIViewVAR2(ListAPIView):
	    """
	    Вар 2, на Дженериках: ListAPIView
	    """
	    queryset = Hero.objects.all().order_by('-id')
	    serializer_class =  ListHeroSerializer

test:
	http://127.0.0.1:8000/heros/
	http://127.0.0.1:8000/herosV2/
		ok!

git add .
git commit -m "added two types of serializers"











делаю дз
myapi/urls.py
	что за
	 path("", include(router.urls)),









🛡 Важные моменты:
Не забудь про валидацию : если пользователь отправит alias, то он должен соответствовать ограничениям (max_length, unique и т.д.)
Если нужно, можно добавить логику валидации в сериализатор, например
def validate_alias(self, value):
    if len(value) > 60:
        raise serializers.ValidationError("Прозвище не может быть длиннее 60 символов.")
    return value
