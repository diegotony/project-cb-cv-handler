.PHONY: clean up-db system-packages python-packages install  run all init

clean:
	rm -r migrations
	rm -r app/main/flask_boilerplate_main.db
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y


python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

up-db:
	python manage.py db init
	python manage.py db migrate --message 'initial database migration'    
	python manage.py db upgrade

run:
	python manage.py run
	# gunicorn -w 4 -b localhost:5000 "manage:app"

all: up-db run