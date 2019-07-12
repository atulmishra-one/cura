## Installation
- Get the clone 
> git clone https://github.com/atulmishra-one/cura.git

- Create virtualenv & activate 
> virtualenv --python=python3 venv
> source venv/bin/activate

- Install requirements
> pip install -r requirements.txt

- Make migrations
> python manage.py makemigrations && python manage.py migrate

- Create super user
> python manage.py createsuperuser

- Run the app
> python manage.py runserver
> http://127.0.0.1:8000