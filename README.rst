toy_py_package
==============

.. image:: https://img.shields.io/pypi/v/toy_py_package.svg
   :target: https://pypi.python.org/pypi/toy_py_package

.. image:: https://img.shields.io/travis/htang085/toy_py_package.svg
   :target: https://travis-ci.com/htang085/toy_py_package

.. image:: https://readthedocs.org/projects/toy-py-package/badge/?version=latest
   :target: https://toy-py-package.readthedocs.io/en/latest/?version=latest
   :alt: Documentation Status

A simple Python package to demonstrate package creation and distribution for DSCI 524.

---

**Free software**: MIT License  
**Documentation**: https://toy-py-package.readthedocs.io  

---

Features
--------

- A simple `add_numbers(a, b)` function that returns the sum of two numbers.
- Example code to demonstrate how to package and distribute a Python project.

Installation
------------

You can install this package from Test PyPI for testing purposes:

.. code-block:: bash

   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple toy_py_package

Usage
-----

Here’s a simple example to demonstrate how to use this package:

.. code-block:: python

   from toy_py_package import add_numbers

   result = add_numbers(2, 3)
   print(result)  # Outputs: 5

Development
-----------

To install this package for development purposes:

.. code-block:: bash

   git clone https://github.com/htang085/toy_py_package.git
   cd toy_py_package
   pip install -e .

To run the tests:

.. code-block:: bash

   python -m unittest discover

TODO
----

- Add more functions to the package.
- Improve testing coverage.

Credits
-------

This package was created with `Cookiecutter`_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage