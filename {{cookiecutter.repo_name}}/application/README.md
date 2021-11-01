# Making applications and APIs with Python

This folder contains three basic templates for an app:

1. A FastAPI webapp, `fastapiwebapp/`
2. A Dash web app, `dashwebapp/`
3. A Flask web app, `flaskwebapp/`

For creating APIs, we recommend using FastAPI.

## Instructions for FastAPI app

The files are under `fastapiwebapp/`. `app.py` is the main entry point and should be customised as needed.

**Requirements:**

- You need the Python package `fastapi`, install through conda by `conda install -c conda-forge fastapi`
  (note it is on channel `conda-forge`).
- You need Python package `uvicorn` ("The lightning-fast ASGI server"), install with conda by `conda install -c conda-forge uvicorn`.

**Run app:**
To run the fastapi app:

```bash
cd fastapiwebapp
uvicorn app:app --reload --port 8886
```

This will boot up the API on port 8886 - go to [localhost:8886](localhost:8886).
_To change default port from 8886, change it in the second command, `uvicorn app:app --reload --port 8886`._

**References:**

- [FastAPI documentation](https://fastapi.tiangolo.com/)

## Instructions for Dash app

The files are under `dashwebapp/`. `app.py` is the main entry point and should be customised as needed.

**Requirements:**

- You need the Python package `dash`, install through conda by `conda install dash`.

**Run app:**
To run the dash app:

```bash
cd dashwebapp
python app.py
```

This will boot up the app on port 8887 - go to [localhost:8887](localhost:8887).
_To change default port from 8887, change it in `dashwebapp/app.py` on the line `app.run_server(debug=True,port=8887)`_

**References:**

- [Dash User Guide](https://dash.plotly.com/)
- [Python Dash Tutorial](https://linuxhint.com/python_dash_tutorial)

## Instructions for Flask app

The files are under `flaskwebapp/` and teh app displays content including Plotly interactive graphs either embedded or hosted online. `app.py` is the main entry point and will server up the template file `templates/layouts/index.html`. Both these files should be customised as needed. You can choose to embed html to display static images or have this generated from python code. The default template uses tabs to swap between content. You can and expand upon the sample to serve multiple pages if so desired. This might be necessary for grouping content or with high memory content.

**Requirements:**

- You need the Python package `flask`, install through conda by `conda install flask`.

**Run app:**
To run the flask app:

```bash
cd flaskwebapp
python app.py
```

This will boot up the app on port 8889 - go to [localhost:8889](localhost:8889).
_To change default port from 8889, change it in `flaskwebapp/app.py` on the line `app.run(host='127.0.0.1', port=8889)`_

**References:**

- [Quickstart to Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Render HTML templates in Flask apps](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)

**Notes:**

- HTML can be embedded into files in the Graph folder. These will be read in and available for embedding as named variables within the template file. Please ensure that you match the file and variable names correctly.
- Note that when using embedded Plotly images you should ensure that the div id elements are unique and match with the contained `Plotly.newPlot()` parameter. If you notice plots not showing up then this could be the reason.
