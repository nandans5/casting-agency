import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


db_drop_and_create_all()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)


    """
    Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    cors = CORS(app)

    """
    Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    # ROUTES

    '''
    GET /actors and /movies
    DELETE /actors/ and /movies/
    POST /actors and /movies and
    PATCH /actors/ and /movies/

    '''

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, movie_id):

        updated_movie = Movie.query.get(movie_id)

        if not updated_movie:
            abort(
                404,
                'Movie with id: ' +
                str(movie_id) +
                ' could not be found.')

        body = request.get_json()

        title = body.get('title', None)
        release_date = body.get('release_date', None)

        if title:
            updated_movie.title = title
        if release_date:
            updated_movie.release_date = release_date

        updated_movie.update()

        return jsonify({
            "success": True,
            "updated": updated_movie.format()
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, actor_id):

        updated_actor = Actor.query.get(actor_id)

        if not updated_actor:
            abort(
                404,
                'Actor with id: ' +
                str(actor_id) +
                ' could not be found.')

        body = request.get_json()

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movie_id = body.get('movie_id', None)

        if name:
            updated_actor.name = name
        if age:
            updated_actor.age = age
        if gender:
            updated_actor.gender = gender
        if movie_id:
            updated_actor.movie_id = movie_id

        try:
            updated_actor.update()
        except BaseException:
            abort(
                400,
                "Bad formatted request due to nonexistent movie id" +
                str(movie_id))

        return jsonify({
            "success": True,
            "updated": updated_actor.format()
        })

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(403)
    def permission_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "permission not allowed"
        }), 403

    @app.errorhandler(401)
    def authError(error):
        return jsonify({
            "success": False, 
            "error": 401,
            "message": "unauthorised"
        }), 401

    @app.errorhandler(AuthError)
    def auth_error(ex):
        print(ex.error['code'], "is the code")
        return jsonify({
            "success": False,
            "error": ex.status_code,
            "message": ex.error['code']
        }),  ex.status_code