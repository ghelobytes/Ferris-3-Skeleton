## Ferris 3 Skeleton

A starter project for using [Ferris 3](http://ferrisframework.org) on Google App Engine.

## Getting started

1. Clone this repository:

    ```
    git clone https://github.com/jonparrott/Ferris-3-Skeleton.git
    cd Ferris-3-Skeleton
    ```

2. Install dependencies using pip:

    ```
    pip install --pre -t lib -r requirements.txt
    ```

3. Run this project locally from the command line. You will need the [App Engine Python SDK](https://developers.google.com/appengine/downloads):

    ```
    dev_appserver.py .
    ```

4. Visit the application's web component [http://localhost:8080](http://localhost:8080)

5. Visit the application's API explorer [http://localhost:8080/_ah/api/explorer](http://localhost:8080/_ah/api/explorer)


## Configuration

Before you develop and deploy your application, you should make some basic changes to the configuration.

1. Edit ``app.yaml`` and change the ``application``.
2. Edit ``app/default-endpoint.yaml`` and fill in your API description and most importantly your application's ``client-id``. You can generate a client id via the [Developers Console](https://console.developers.google.com).
