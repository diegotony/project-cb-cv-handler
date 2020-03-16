clean:
	rm -r migrations
	rm -r app/main/flask_boilerplate_main.db

up-server:
	python manage.py db init
	python manage.py db migrate --message 'initial database migration'    
	python manage.py db upgrade
	python manage.py run


.PHONY: clean up-server 