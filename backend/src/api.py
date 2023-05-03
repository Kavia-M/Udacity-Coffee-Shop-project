import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import traceback

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# To be commented from 2nd run or else the database would be reset
db_drop_and_create_all()

# ROUTES

'''
@requires_auth() is not needed for this end point.
It is public. Anyone even without token can view it.
'''
@app.route('/drinks')
def get_drinks():
    '''
    Endpoint to view the drinks. Since It is a public endpoint
    Anyone can view even without loggin in.
    '''
    drinks_list = Drink.query.order_by(Drink.id).all()
    drinks = [drink.short() for drink in drinks_list]
    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    '''
    Endpoint to get a detailed view of the drinks
    '''
    drinks_list = Drink.query.order_by(Drink.id).all()
    drinks = [drink.long() for drink in drinks_list]
    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    '''
    Endpoint to create a new drink
    '''
    body = request.get_json()
    new_title = body.get("title", None)
    new_recipe = body.get("recipe", [])

    if not new_title or not new_recipe:
        abort(400)  # Bad request since body is not in requied format

    new_recipe = str(new_recipe)  # since list cannot be used in SQL prepared statememts
    new_recipe = new_recipe.replace("'", '"')  # frontend sends recipe with ' that is to be replaced with "

    try:
        drink = Drink(title=new_title, recipe=new_recipe)
        drink.insert()

        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        })
    except Exception as e:
        traceback.print_exc()  # useful for debugging
        abort(422)  # unexpected errors


@app.route("/drinks/<int:id>", methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, id):
    body = request.get_json()
    print(body)
    new_title = body.get("title", None)
    new_recipe = body.get("recipe", [])

    if not new_title and not new_recipe:
        abort(400)  # Bad request since body is not in requied format

    new_recipe = str(new_recipe)  # since list cannot be used in SQL prepared statememts
    new_recipe = new_recipe.replace("'", '"')  # frontend sends recipe with ' that is to be replaced with "

    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if drink is None:
        abort(404)  # 404 not found if a drink with the id is not in database
    drink.title = new_title
    drink.recipe = new_recipe
    try:
        drink.update()

        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        })
    except Exception as e:
        traceback.print_exc()  # useful for debugging
        abort(422)  # unexpected errors


@app.route("/drinks/<int:id>", methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    if drink is None:
        abort(404)  # 404 not found if a drink with the id is not in database
    try:
        drink.delete()

        return jsonify({
            "success": True,
            "delete": id
        })
    except Exception as e:
        traceback.print_exc()  # useful for debugging
        abort(422)  # unexpected errors

# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    '''
    error handling for unprocessable entity
    '''
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    '''
    error handler for 404 not found
    '''
    return (
        jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404,
    )


@app.errorhandler(405)
def method_not_allowed(error):
    '''
    error handler for 405 method not allowed
    '''
    return (
        jsonify({"success": False, "error": 405, "message": "method not allowed"}),
        405,
    )


@app.errorhandler(400)
def bad_request(error):
    '''
    error handler for 400 bad request 
    '''
    return jsonify({"success": False, "error": 400, "message": "bad request"}), 400


@app.errorhandler(500)
def internal_server_error(error):
    '''
    error handler for 500 internal server error
    '''
    return jsonify({"success": False, "error": 500, "message": "internal server error"}), 500


@app.errorhandler(AuthError)
def handle_auth_error(exeption):
    '''
    error handler for AuthError
    '''
    response = jsonify(exeption.error)
    response.status_code = exeption.status_code
    return response
