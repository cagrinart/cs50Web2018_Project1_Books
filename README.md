# Project 1

Web Programming with Python and JavaScript

# To Run The Project
1. Create virtual environment with the following commands from terminal
  * pip install virtualenv
  * python3 -m venv cs50hw1
  * source cs50hw1/bin/activate
  * deactivate - for deactivating venv
  * which python - check which python env in use

2. Install dependencies
  * pip3 install -r requirements.txt

3. Set enviroment variables
  * export DATABASE_URL=******
  * export FLASK_APP=application.py
  * export FLASK_DEBUG=1

4. To run application.py
  * flask run

  If there is an error like "Can't load plugin: sqlalchemy.dialects:postgres"; rename `postgres://` in the URI to `postgresql://`
