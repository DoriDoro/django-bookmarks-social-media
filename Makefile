secret_key:
	python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

shell:
	python manage.py shell

create_db:
	python manage.py makemigrations
	python manage.py migrate

server:
	python manage.py runserver
