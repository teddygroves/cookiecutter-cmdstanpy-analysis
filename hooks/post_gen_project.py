import os
from shutil import rmtree

REMOVE_PATHS = [
    '{% if cookiecutter.create_writing_directory != "y" %} writing {% endif %}',
    '{% if cookiecutter.create_tests_directory != "y" %} tests {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        rmtree(path)
