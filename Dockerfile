FROM python:3.6
EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
COPY . /usr/src/app/
RUN chmod +x manage.py
# RUN python manage.py db init
# RUN	python manage.py db migrate --message 'initial database migration'    
# RUN	python manage.py db upgrade
RUN chmod +x entrypoint.sh

CMD ["/bin/bash", "entrypoint.sh"]]
