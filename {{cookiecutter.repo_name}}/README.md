# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}


## Setup

1. Install git and checkout the [git code repository]
2. Install [anaconda] python version 3.6+
3. Change working directory into the git code repository root
4. Create the self contained conda environment;
    - Change the environment name in the file `conda_env.yml` (default name is `my_environment`)
    - Add other necessary packages to `conda_env.yml` under dependencies.
    - Go to the git code repository root and enter the command:

        ```bash
        conda env create --file conda_env.yml
        ```

    - Activate the conda environment:

        ```bash
        conda activate my_environment
        ```

    - To make the environment available as a kernel in Jupytyer notebook, 
      install an ipython kernel by

        ```bash
        python -m ipykernel install --user --name my_environment --display-name "Python (my_environment)"
        ```

        Feel free to change the naming here as well.

5. Any python modules under folder `src/` need to be available to other scripts. 
Install the module locally (in developer mode) in your conda environment with modifications
reflected immediately:

    ```bash
   pip install -e .
    ```


## Initial File Structure

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── application              <- Application
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
│   ├── interim_[desc]       <- Interim files - give these folders whatever name makes sense.
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   └── temp                 <- Temporary files.
│
├── docs                     <- Documentation
│   └── writeup              <- Sphinx project for project writeup including auto generated API.
│       ├── conf.py          <- Sphinx configurtation file.
│       ├── index.rst        <- Start page.
│       ├── make.bat         <- For generating documentation (Windows)
│       └── Makefile         <- For generating documentation (make)
│
├── extras                   <- Miscellaneous extras.
│   └── add_explorer_context_shortcuts.reg    <- Adds additional Windows Explorer context menus for starting jupyter.
│
├── notebooks                <- Notebooks for analysis and testing
│   ├── eda                  <- Notebooks for EDA
│   ├── features             <- Notebooks for generating and analysing features (1 per feature)
│   ├── modelling            <- Notebooks for modelling
│   └── preprocessing        <- Notebooks for Preprocessing 
│
├── scripts                  <- Standalone scripts
│   └── example.py           <- Example script
│
├── src                      <- Code for use in this project.
│   └── {{cookiecutter.package_name}}       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    └── {{cookiecutter.package_name}}       <- {{cookiecutter.package_name}} tests
        └── examplemodule    <- examplemodule tests (1 file per method tested)
```

## Testing

Reproducability and the correct functioning of code are essential to avoid wasted time. 
If a code block is copied more than once then it should be placed into a 
common script / module under `src/` and unit tests added. The same applies for 
any other non trivial code to ensure the correct functioning.

To run tests, install `pytest` using pip or conda (should have been setup already if 
you used the `conda_env.yml` file) and then from the repository root run
 
```bash
pytest
```

## Automated Document Generation

A [sphinx](https://www.sphinx-doc.org/) project is provided under `docs/writeup/` that will generate writeup that
also includes automatically generated API information for any packages. The output can be created in multiple
formats including html and pdf. If you are using CI then this can be run automatically. 
To run locally execute the following commands:

```bash
cd docs/writeup
make html
```

On Windows this will run the `make.bat`, a Makefile is also included for those using the `make` command.


[//]: #
   [anaconda]: <https://www.continuum.io/downloads>
