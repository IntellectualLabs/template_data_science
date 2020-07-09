"""
This is the {{cookiecutter.package_name}} API documentation.
"""

# Import standard modules
import time

# Import 3rd party modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import custom modules
from {{cookiecutter.package_name}}.examplemodule import hello_world
from {{cookiecutter.package_name}}.timing_utils import setup_logger

LOGGER = setup_logger("root")
app = FastAPI()

# For now we will allow any website to access the API,
# which will let us access it on localhost:
# from a javascript script
# NOTE: this should be changed when in prod;
#     only allow access from {{cookiecutter.project_name}} websites/apps
#     See https://fastapi.tiangolo.com/tutorial/cors/
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Welcome to the {{cookiecutter.package_name}} api!"}


@app.get("/hello")
def hello_app(name: str = None):
    """

    Arguments:
    ----------
    - name : string
        - name of API user

    Returns:
    --------
    - hello_back : str
    - hello_generic : str
    """
    time.sleep(0.5)
    hello_back = "Hello " + name + " from {{cookiecutter.package_name}}"
    hello_generic = hello_world()

    return {"reply": hello_back, "reply_world": hello_generic}


if __name__ == "__main__":
    print("app.py was run")
