web: gunicorn -w 4 -b localhost:5000 "manage:app"
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py upgrade