
help:
	@echo "init-db           - init database "
	@echo "run               -  run  project"
	@echo "env               - create envioroment"
	@echo "clean env         - remove enviroment"
	@echo "pip-install_req   - install requirements"



env:
	virtualenv -p python3.7 $@
	${MAKE} pip-install-req


pip-install-req:
	env/bin/pip install -r requirements.txt

clean_env:
	rm -rdvf env

init-db:
	python manage.py db init
	python manage.py db migrate --message 'initial database migration'    
	python manage.py db upgrade

run:
	# python manage.py runserver --host 0.0.0.0 --port ${PORT}
	python manage.py runserver --host 0.0.0.0 

# TODO: docker-compose command
