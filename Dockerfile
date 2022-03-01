FROM python:3.9.0

WORKDIR /home/

RUN echo wb12


RUN git clone https://github.com/ssorn88/whobetter.git

WORKDIR /home/whobetter/



RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

RUN export DJANGO_SUPERUSER_EMAIL=admin

RUN export DJANGO_SUPERUSER_PASSWORD=admin

RUN export DJANGO_SETTINGS_MODULE=whobetter.settings.deploy




CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=whobetter.settings.deploy && python manage.py migrate --settings=whobetter.settings.deploy && python manage.py createsuperuser --no-input --settings=whobetter.settings.deploy &&  gunicorn whobetter.wsgi --env DJANGO_SETTINGS_MODULE=whobetter.settings.deploy --bind 0.0.0.0:8000"]