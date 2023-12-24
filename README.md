# flask_hello_world

Minimum viable product for a Flask app deployed on Render.

## Minimum Requirements
* [Python 3.11.6](https://www.python.org/downloads/release/python-3116/)
* [Pip](https://pip.pypa.io/en/stable/installing/)

## Recommended Requirements
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://docs.docker.com/get-docker/)
* [asdf](https://asdf-vm.com/#/core-manage-asdf-vm)
    ```bash
    # install python
    asdf plugin add python
    asdf install python 3.11.6

    # install poetry
    asdf plugin add poetry
    asdf install poetry 1.7.1
    ```

## Quickstart
* Python
    ```bash
    # create virtual environment
    python -m venv .venv
    source .venv/bin/activate

    # install requirements
    python -m pip install -r requirements.txt

    # run the app
    python app.py
    ```
* Python + Poetry
    ```bash
    # install requirements
    poetry install

    # run the app
    poetry run python app.py
    ```
* Docker
    ```bash
    # build the image
    docker build -t flask_hello_world .

    # run the image
    docker run -p 8000:8000 flask_hello_world       # stop via ctrl+c

    # run the image in detached mode
    docker run -d -p 8000:8000 flask_hello_world

    # stop the container
    docker stop <container_id>
    ```

## TODO
* [Issues](https://github.com/pythoninthegrass/flask_hello_world/issues)

## Further Reading
[Deploy a Flask App | Render Docs](https://render.com/docs/deploy-flask)
