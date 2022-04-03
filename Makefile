up:
	docker-compose up -d --build

down:
	docker-compose down


dev: 
		docker-compose up -d --build mailhog; export FLASK_APP=main.py; export FLASK_ENV=development; export FLASK_DEBUG=1; flask run --port=3000


