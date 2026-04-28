[New with Django]
Project = Ironcrew
App1 = homePage

# Starting the app 
cd djangoAkola 
python manage.py runserver

# Running the app with Gunicorn (use Nginx to load images)
cd djangoAkola
gunicorn ironcrew.wsgi:application --bind 0.0.0.0:8000


# Ngnix config
Add this erver details in nginx.conf - 

server {
        listen       8082;
        server_name  localhost;

location = /favicon.ico { access_log off; log_not_found off; }

# Serve static files
location /static/ {
        alias /Users/hiteshambarkhane/Documents/Website/portal/akola/djangoAkola/staticfiles/;
        # autoindex on;
    }

  # Proxy requests for specific paths to the backend
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


[OLD]
To setup dev environment -

Install git, python3, virtual env

python3 -m venv .akola
source .akola/bin/activate

When installing first time, install the requirements -
pip install -r requirements.txt

Run this to start the website -

uvicorn main:app --reload --host 0.0.0.0 --port 8000


