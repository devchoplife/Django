# Useful commands when working with Django

python3 -m venv <virtual-environment-name> # Create virtual environment 
python3 -m pip install django # install django on virtual environment
django-admin --version # Check sjango version/to also check if django is installed 
pip freeze # This can also show you if django is installed 
django-amin startproject <project-name> # Create a new django project
python3 <project-dir>/manage.py runserver # start the server so you can see your live website 
python3 <project-dir>/manage.py startapp <app-name> # create a new django application
python3 <project-dir>/manage.py makemigrations <app-name> # Create migrations after making changes to the table or database
python3 <project-dir>/manage.py migrate # make the migration