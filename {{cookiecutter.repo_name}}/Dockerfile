# The Docker image default will expose the app in application/app.py
# through port 80. The docker image will
#   1) rebuild the conda environment as defined
#      through conda_env.yml and also copy over
#   2) install the local package, i.e. run setup.py
#      (which will need src/ and README.md)
#   3) Run the fastAPI app, application/app.py, and make it
#      available through port 80
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

# Make sure the environment is activated:
RUN echo "Make sure {{cookiecutter.package_name}} is installed:" && \
    python -c "import {{cookiecutter.package_name}}"

# The code to run when container is started:
COPY application/app.py app.py

# Add some labels
LABEL maintainer="{{cookiecutter.author}}"

# Expose app.py in port 80
EXPOSE 80
CMD uvicorn app:app --host 0.0.0.0 --port 80
