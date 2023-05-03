# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### Implemention In The Server
    The files I modified in backend
1. `./src/auth/auth.py`
2. `./src/api.py`
3. `./src/database/models.py` - added a command to avoid errors
4. **`./udacity-fsnd-udaspicelatte.postman_collection.json`** - This is uploaded after overwriting in Postman with my JWTs. ***NOTE : The JWT will expire in 24 hours***

### API Reference
Errors are returned as JSON objects in the following format:
```json
{
    "success" : false,
    "error": 404,
    "message": "resource not found"
}
```
The possible errors are:

Error code | Error type |
--- | --- |
400 | Bad request
401 | Unauthorized
403 | Forbidden
404 | Resource Not Found
405 | Method not allowed
422 | Unprocessable
500 | Internal Server Error

The Endpoints are 

#### `GET '/drinks'`
- General:
    - Returns success and the list of drinks
    - This is used to display the drinks in menu
- **Permission** : 
    - ***no permissin needed*** - It's a public endpoint, anyone can view even without login. 

#### `GET '/drinks-detail'`
- General:
    - Returns success and the list of drinks with detailed recipe
    - This is used by barista to prepare coffee
- **Permission** : 
    - ***'get:drinks-detail*** - Can be used by Manager

#### `POST '/drinks'`
- General:
    - Returns success and the list with only the drink that is just created 
    - This is used manager to create a new drink
- **Permission** : 
    - ***'post:drinks*** - Can be used by Manager

#### `PATCH '/drinks'`
- General:
    - Returns success and the list with only the drink that is just edited 
    - This is used manager to edit an existing drink
- **Permission** : 
    - ***'patch:drinks*** - Can be used by Manager

#### `DELETE '/drinks'`
- General:
    - Returns success and the id of the drink that is just deleted 
    - This is used manager to delete an existing drink
- **Permission** : 
    - ***'delete:drinks*** - Can be used by Manager
