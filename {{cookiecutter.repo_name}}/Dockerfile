{% if cookiecutter.python_package_manager == 'conda' %}
# The Docker image default will expose the app in application/app.py
# through port 80. The docker image will
#   1) rebuild the conda environment as defined
#      through conda_env.yml
#   2) install the local package, i.e. run setup.py
#      (which will need src/ and README.md)
#   3) Run the fastAPI app, application/app.py, and make it
#      available through port 80
#
# NOTE: The conda docker image is not very lightweight, and it is
#       good practice to rather use a more lightweight Python image
#       with standard pip install (from requirement.txt file)
#
# Refs:
# - https://pythonspeed.com/articles/activate-conda-dockerfile/
FROM continuumio/miniconda3

WORKDIR /app

# Install needed Ubuntu stff to enable pip install jsonnet
#    Ref: https://github.com/google/jsonnet/issues/756
#RUN apt-get update && \
#    apt-get -y install build-essential

# Create the environment:
COPY conda_env.yml env.yml
RUN conda env create -f env.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "{{cookiecutter.project_name.lower().replace(' ', '_')}}", "/bin/bash", "-c"]

# Install local library
RUN echo "Installing local package {{cookiecutter.package_name}}:"
COPY README.md .
COPY setup.py .
COPY src src
RUN pip install -e .

# Make sure the local package is activated:
RUN echo "Make sure {{cookiecutter.package_name}} is installed:" && \
    python -c "import {{cookiecutter.package_name}}"

# The code to run when container is started:
COPY application/fastapiwebapp/app.py app.py

# Add some labels
LABEL maintainer="{{cookiecutter.author}}"

# Expose app.py in port 80
EXPOSE 80
CMD uvicorn app:app --host 0.0.0.0 --port 80

{% elif cookiecutter.python_package_manager == 'poetry' %}
# The Docker image default will expose the app in application/app.py
# through port 80. The docker image will
#   1) rebuild the poetry environment as defined
#      in pyproject.toml and poetry.lock
#   2) install the local package, i.e. run setup.py
#      (which will need src/ and README.md)
#   3) Run the fastAPI app, application/app.py, and make it
#      available through port 80
#
# NOTE: The poetry docker image is not very lightweight (even if
#       it is more lightweight than the conda image), and it is
#       good practice to rather use a more lightweight Python image
#       with standard pip install (from requirement.txt file).
FROM python:3.8.2-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git build-essential curl wget && \
    pip install --upgrade pip

COPY poetry.lock pyproject.toml /app/
COPY README.md .
COPY setup.py .
COPY src src

# Install local library
RUN echo "Installing poetry environment and local package {{cookiecutter.package_name}}:" && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-dev

# Make sure the local package is activated:
RUN echo "Make sure {{cookiecutter.package_name}} is installed:" && \
    python -c "import {{cookiecutter.package_name}}"

# The code to run when container is started:
COPY application/fastapiwebapp/app.py app.py

# Add some labels
LABEL maintainer="{{cookiecutter.author}}"

# Expose app.py in port 80
EXPOSE 80
CMD uvicorn app:app --host 0.0.0.0 --port 80

{% endif %}
