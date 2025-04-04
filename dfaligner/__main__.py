"""
This file turns the package into a module that can be run as a script with
    python -m dfaligner ...
or, for coverage analysis, with
    coverage run -m dfaligner ...
"""

from .cli import app

app()
