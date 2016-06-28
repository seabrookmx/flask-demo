# flaskdemo
Demo flask RESTful Api - inspired by the flaskr demo in Flask's sample code.

## To run though the console, set up your virtualenv by running:
`python3 -m virtualenv venv` If your default installation of python is python3, then you can simply run `python -m virtualenv venv`

## Activate your virtualenv by running:
`source venv/bin/activate` This needs to be done in every new terminal where you plan to interact with Python

## Ensure you're running the right interpreter (this should return 3.x)
`python --version`

## Install dependencies:
`pip install -r requirements.txt`

## To debug, run "flaskdemo.py":
`python flaskdemo.py`

## When running flaskdemo.py, you should be able to hit some API routes:
`http://localhost:5000/api/Entries`

`http://localhost:5000/api/Entries/1`

 with either curl or the Advanced Rest Client.
