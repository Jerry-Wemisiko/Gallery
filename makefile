serve:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations photos
	
migrate:
	python3 manage.py migrate

collectstatic:
	python3 manage.py collectstatic