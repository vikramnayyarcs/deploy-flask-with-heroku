# deploy-flask-with-heroku
Sample app for deploying Flask with Heroku.

New directory
python3 -m venv venv

Activate VENV:
	MAC OS/Linux: source venv/bin/activate
	Windows: venv\Scripts\activate

Install Flask
Pip Freeze - (requirements.txt)
Create App.py

Setup Flask ENV:
	MAC: export FLASK_ENV=development
	Windows: set FLASK_ENV=development

Git init

Heroku Deployment:
Install Heroku CLI (I found using npm easier)
Heroku login

Procfile in root ( echo "web: gunicorn app:app" > Procfile ) ** Create in Notepad++ on Windows.

Gunicorn - Python server web interface

python3 -m pip install gunicorn==20.0.4
python3 -m pip freeze > requirements.txt

heroku create APP_NAME

git push heroku master
