# Testing

Reproducability and the correct functioning of code are essential to avoid wasted time.
If a code block is copied more than once then it should be placed into a
common script / module under `src/` and unit tests added. The same applies for
any other non trivial code to ensure the correct functioning.

## Run tests with `pytest`
To run tests, ensure you have installed the conda environment as explained above
(from `conda_env.yml`) and activated it.

*If not, install `pytest`, `pytest-cookies`, `pytest-cov`,
`pytest-remotedata==0.3.2` using pip or conda.*

Then from the repository root run

```bash
pytest tests\
```

After initial repo creation, i.e. using the cookiecutter instructions,
the result of running this should display the following in terminal:

```python
<your-root-parent-dir>/{{cookiecutter.repo_name}}>pytest tests\
========================================== test session starts ==========================================
platform win32 -- Python 3.8.6, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: <your-root-parent-dir>/{{cookiecutter.repo_name}}
plugins: cookies-0.5.1, cov-2.10.1, remotedata-0.3.2
collected 8 items

tests\test_randomtests.py .F...                                                                    [ 62%]
tests\{{cookiecutter.package_name}}\test_examplemodule.py ...                                      [100%]

=============================================== FAILURES ================================================
____________________________________________ test_that_fails ____________________________________________

    def test_that_fails():
>       assert False, "We expected this to fail"
E       AssertionError: We expected this to fail
E       assert False

tests\test_randomtests.py:6: AssertionError
======================================== short test summary info ========================================
FAILED tests/test_randomtests.py::test_that_fails - AssertionError: We expected this to fail
====================================== 1 failed, 7 passed in 0.55s ======================================
```

*Note that `<your-root-parent-dir>` willl be replaced by your repos parent directory.*

## Run tests and display test coverage
To display test coverage of all source code in the folder `src/` run from repository root

```bash
pytest --cov-report term-missing --cov=src tests\
```

After initial repo creation, i.e. using the cookiecutter instructions,
the result of running this should display the following in terminal:

```python
<your-root-parent-dir>/{{cookiecutter.repo_name}}>pytest --cov-report term-missing --cov=src tests\
========================================== test session starts ==========================================
platform win32 -- Python 3.8.6, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: <your-root-parent-dir>/{{cookiecutter.repo_name}}>
plugins: cookies-0.5.1, cov-2.10.1, remotedata-0.3.2
collected 8 items

tests\test_randomtests.py .F...                                                                    [ 62%]
tests\{{cookiecutter.package_name}}\test_examplemodule.py ...                                      [100%]

=============================================== FAILURES ================================================
____________________________________________ test_that_fails ____________________________________________

    def test_that_fails():
>       assert False, "We expected this to fail"
E       AssertionError: We expected this to fail
E       assert False

tests\test_randomtests.py:6: AssertionError

----------- coverage: platform win32, python 3.8.6-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------------
src\{{cookiecutter.package_name}}\__init__.py            0      0   100%
src\{{cookiecutter.package_name}}\examplemodule.py       7      1    86%   41
src\{{cookiecutter.package_name}}\timing_utils.py       21     21     0%   5-58
------------------------------------------------------------------------------------
TOTAL                             28     22    21%

======================================== short test summary info ========================================
FAILED tests/test_randomtests.py::test_that_fails - AssertionError: We expected this to fail
====================================== 1 failed, 7 passed in 0.53s ======================================
```

The term `--cov-report term-missing` will show which lines of each `.py`-file in `src/`
that are not covered by tests.


## References
- [realpython - Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [realpython - Effective Python testing with `pytest`](https://realpython.com/pytest-python-testing/)
- [`pytest-cov` docs](https://pytest-cov.readthedocs.io/en/latest/readme.html#documentation)