create virtual enviroment

git bash

freez 


sabay intall django



rm -rf env  # Deletes the broken environment
python -m venv env  # Creates a new one
source env/Scripts/activate  # Activate it
pip install --upgrade pip  # Upgrade pip
pip install psycopg
pip install psycopg2
python manage.py runserver
pip install django

if abaove does not workaround
pip install django
pip install psycopg2
pip install psycopg2-binary
python -c "import psycopg" or python -c "import psycopg2"



python manage.py runserver