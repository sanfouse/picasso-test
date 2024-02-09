migrate:
	python manage.py migrate

create-superuser:
	python manage.py createsuperuser --no-input

collect-static:
	python manage.py collectstatic --no-input

shell:
	python manage.py shell