start:
	docker-compose up -d
up:
	docker-compose up
down:
	docker-compose down
stop:
	docker-compose stop
build:
	docker-compose build
migrate:
	docker exec -it testing_task_python_container alembic upgrade head
enter_db:
	docker exec -it testing_task_db_container psql --username=core_db_user --dbname=core_db
enter_web:
	docker exec -it testing_task_python_container sh
reset: down start migrate stop up