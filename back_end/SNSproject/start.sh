sleep 5
cd /
cd /home/testuser1/dev/SNSproject
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
uwsgi --socket :8001 --module SNSproject.wsgi