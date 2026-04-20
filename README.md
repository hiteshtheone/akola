[New with Django]
Project = Ironcrew
App1 = homePage


[OLD]
To setup dev environment -

Install git, python3, virtual env

python3 -m venv .akola
source .akola/bin/activate

When installing first time, install the requirements -
pip install -r requirements.txt

Run this to start the website -

uvicorn main:app --reload --host 0.0.0.0 --port 8000


