mig:
	./manage.py makemigrations
	./manage.py migrate

admin:
	python3 manage.py createsuperuser --noinput