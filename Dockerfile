FROM python:3.9.0

WORKDIR /home/

RUN echo wb13


RUN git clone https://github.com/ssorn88/whobetter.git

WORKDIR /home/whobetter/



RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'es4402@korea.ac.kr', 'admin')" | python manage.py shell


EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=whobetter.settings.deploy && python manage.py migrate --settings=whobetter.settings.deploy && gunicorn whobetter.wsgi --env DJANGO_SETTINGS_MODULE=whobetter.settings.deploy --bind 0.0.0.0:8000"]