build:
	docker-compose build
	
up:
	docker-compose up

down: 
	docker-compose down

migrate:
	docker-compose exec web python manage.py migrate

load_data:
	docker-compose exec web python manage.py loaddata users_data.json

shell:
	docker-compose exec web python manage.py shell

makemigrations:
	docker-compose exec web python manage.py makemigrations

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

test:
	docker-compose exec web python manage.py test
