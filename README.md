# flaskdemo
Demo flask RESTful Api - inspired by the flaskr demo on Flask's github and docs.

## To run though the console, set up your virtualenv by running:
`virtualenv venv`

## Activate your virtualenv by running (this needs to be done in every new terminal you plan to run the app from):
`source venv/bin/activate`

## Install dependencies:
`pip3 install -r requirements.txt`

## To debug, run "flaskdemo.py":
`python3 flaskdemo.py`  # may be just "python" depending on your system

## When running flaskdemo.py, you should be able to hit some API routes:
`http://localhost:5000/api/Entries`

`http://localhost:5000/api/Entries/1`

 with either curl or the Advanced Rest Client.
