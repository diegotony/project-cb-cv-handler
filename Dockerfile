FROM python:3.6
EXPOSE 5000
WORKDIR /usr/src/app
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
COPY . /usr/src/app/
RUN chmod +x manage.py
ENV PORT=5000
RUN python manage.py runserver --host 0.0.0.0 --port ${PORT}
CMD ["/bin/bash", "entrypoint.sh"]]
