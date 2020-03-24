.PHONY: clean up-db system-packages python-packages install  run all init

env:
	virtualenv -p python3.7 $@
	${MAKE} python-install-req


python-install-req:
	env/bin/pip install -r requirements.txt

clean_env:
	rm -rdvf env

up-db:
	python manage.py db init
	python manage.py db migrate --message 'initial database migration'    
	python manage.py db upgrade

run:
	python manage.py runserver --host 0.0.0.0 --port ${PORT}

