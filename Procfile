release: python manage.py migrate
web: gunicorn gettingstarted.wsgi --log-file -
worker: python manage.py runworker channels --settings=FundForLectures.settings -v2