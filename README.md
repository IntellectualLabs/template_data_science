# Data Science Template

This is a starter template for data science projects in Intellectual Labs.

As it is impossible to create a single template that will meet every projects needs,
this example should be considered
a starting point and changed based upon the working and evolution of your project.

This template builds upon the [data science template provided by Equinor](https://github.com/equinor/data-science-template), which in turn builds on a [Cookiecutter template](http://cookiecutter.readthedocs.org/en/latest/installation.html).


## Getting Started With This Template

This template is provided as a [Cookiecutter template](http://cookiecutter.readthedocs.org/en/latest/installation.html) so you
can quickly create an instance customised for your project. An assumption is that you have a working python installation.

To get running, first install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

### Create project

Then generate a new project for your own use based upon the template, answering the questions to customise the generated project:

```bash
cookiecutter https://github.com/IntellectualLabs/data_science_template
```

The values you are prompted for are:

| Value                   | Description |
| :---                    | --- |
| project_name            | A name for your project. Used mostly within documentation |
| project_description     | A description to include in the README.md |
| repo_name               | The name of the github repository where the project will be held |
| package_name            | A name for the generated python package. |
| author                  | The main author of the solution. Included in the setup.py file |
| open_source_license     | What type of open source license the project will be released under |

If you are uncertain about what to enter for any value then just accept the defaults.
You can always change the generated project later.

You are now ready to get started, however you should first create a new
github repository for your new project and add your project using the following commands
(substitute `myproject` with the name of your project and REMOTE-REPOSITORY-URL
with the remote repository url).

```bash
cd myproject
git init
git add .
git commit -m "Initial commit"
git remote add origin REMOTE-REPOSITORY-URL
git remote -v
git push origin master
```

Finally update the project readme file, `README.md`, with additional project specific details
including setup, configuration and usage.


## Generated Project Contents

Depending upon the selected options when creating the project, the generated structure will look similar to the below:

```
├── .gitignore               <- Files ignored by git. Add seperate .gitignore files in sub folders if needed
├── .dockerignore            <- Files that should be ignored when building the docker image from Dockerfile
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── Dockerfile               <- File defining how to build the docker image
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── application              <- Application
|   ├── app.py               <- FastAPI application
|   ├── README.md
│   ├── dashwebapp           <- Application template using dash
│   │   ├── assets           <- Web tech asset files; css layout files and js
│   │   │   └── header.css   <- Layout css file for header
│   │   └── app.py           <- Application file
│   └── webapp               <- Application template using flask
│       ├── Graph            <- Text files with some html graphs
│       ├── static           <- Static files, e.g. pdfs
│       ├── templates        <- Template files
│       │   └── layouts      <- Layout files
│       │      └── index.html  <- Example index html file
│       └── app.py           <- Application file
│
├── data
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   └── temp                 <- Temporary files.
│
├── docs                     <- Documentation
│   ├── images               <- Image files for documentation
│   │   └── ILlogo.png       <- Intellectual Labs logo
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│       ├── conf.py          <- Sphinx configurtation file.
│       ├── index.rst        <- Start page.
│       ├── make.bat         <- For generating documentation (Windows)
│       └── Makefile         <- For generating documentation (make)
│
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   │   └── example.ipynb    <- Example python notebook
│   └── modelling            <- Notebooks for modelling
│
├── scripts                  <- Standalone scripts
│   └── example.py           <- Example script
│
├── src                      <- Code for use in this project.
│   └── {{cookiecutter.package_name}}       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       └── timing_utils.py  <- Functions for timing and logging
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    └── {{cookiecutter.package_name}}       <- {{cookiecutter.package_name}} tests
        └── examplemodule    <- examplemodule tests (1 file per method tested)
```


## References

* https://github.com/Statoil/data-science-template/
* http://docs.python-guide.org/en/latest/writing/structure/
* https://drivendata.github.io/cookiecutter-data-science/
* https://github.com/audreyr/cookiecutter-pypackage

[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
