# Flask server to run Poker AI API

This is a stateless server. Which means that the service is tolerant of any interruptions in the server.

If, in the future, we would like to save some information for the AI as well, we should either use the file-system, or a database service like redis or mongodb.

## Setting up

Make sure that you are using a virtual environment for all your work in this directory.
You can install all the required packages in your virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Development

Start this server in development mode using the following commands:
```
./run.sh
```

## Deploying on GCP

Make sure that you have `gcloud` CLI installed in your terminal (refer: [AppEngine Documentation](https://cloud.google.com/appengine/docs/standard/python3/testing-and-deploying-your-app))

Also make sure that `gcloud` is configured to the staging project.
```
gcloud config set project getmega-app
```

### Before you deploy
You can test your deployment locally by using the `dev_appserver.py` command that comes pre-installed with `gcloud`. Run the following command to test:
```
dev_appserver.py --runtime_python_path=.venv/bin/python3 .
```

### Deploy
Now you can run the following command to deploy this on Google App Engine:
```
gcloud app deploy
```
