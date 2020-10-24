# Stataflow-CS235-Flix

COMPSCI235 Movie 'Flix' Application

## Cloud Deployment

As well as being able to run a local version of my code with a memory database, I have deployed a version of my code to a cloud instance in Google Cloud Platform that uses google cloud sql as the database

You can view it here: http://www.stataflow.com

## Running a local version

**NOTE** You will require 2 terminal windows to run this application locally due to the frontend running in React JS and the backend running in Flask

**NOTE** To ensure that the script that starts the virtuan env works, you will need to open the terminals in administrator mode.

### Windows Process

#### Terminal 1 (backend)

Navigate to 'Statflow-CS235-Flix' -> `cd ~/Stataflow-CS235-Flix`

Move into 'backendflask' -> `cd /backendflask`

Activate venv -> `.\venv\Scripts\activate`

**NOTE** If you get an error telling you scripts cannot be loaded, you can enter `Set-ExecutionPolicy RemoteSigned` to allow the script to run, and then `Set-ExecutionPolicy Restricted` when you are done.

Install requirements -> `pip3 install -r requirements.txt`

Run tests -> `pytest` or `pytest .\testing`

Setting environment variable -> `set FLASK_APP=main`

Starting the backend -> `flask run`

#### Terminal 2 (frontend)

**NOTE** If you run `npm -v` and do not get a result, you will need to install Node or just view it from the cloud deployment

Node download here: https://nodejs.org/en/download/

Navigate to 'Statflow-CS235-Flix' -> `cd ~/Stataflow-CS235-Flix`

Move into 'frontend-react' -> `cd /frontend-react`

Installing dependencies -> `npm i`

Start the front end -> `npm start`

## Unix Install Process (for local use)
