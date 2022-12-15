build:
	docker-compose build
	
up:
	docker-compose up

down: 
	docker-compsoe down

migrate:
	docker-compose exec web python manage.py migrate

createsuperuser:
	docker-compose exec web python manage.py createsuperuser
