#!/bin/sh

python manage.py db init
python manage.py db migrate  --message 'initial database migration'    
python manage.py db upgrade

# gunicorn -w 4 -b localhost:5000 "manage:app"
python manage.py run