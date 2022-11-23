# add actor and movie ids in post endpoints (foreign tables)
# add actor and movie ids in patch endpoints (foreign tables)
import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

from models import *
from auth import AuthError, requires_auth

# db_drop_and_create_all()

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
    # GET movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = Movie.query.order_by(Movie.id).all()
        format_movies = [i.format() for i in movies]

        return jsonify({
            'movies':format_movies
        })

    # GET actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = Actor.query.order_by(Actor.id).all()
        format_actors = [i.format() for i in actors]

        return jsonify({
            'actors':format_actors
        })

    # DELETE movie
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, id):
        try:
            selection = Movie.query.filter(Movie.id == id).one_or_none()

            if selection is None:
                abort(404)
                
            selection.delete()

            return jsonify({
                'success': True
            })

        except:
            abort(422)

    # DELETE actor
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, id):
        try:
            selection = Actor.query.filter(Actor.id == id).one_or_none()

            if selection is None:
                abort(404)
                
            selection.delete()

            return jsonify({
                'success': True
            })

        except:
            abort(422)

    # POST movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_month = body.get('release_month', None)

        try:
            movie = Movie(title=new_title, release_month=new_release_month)
            movie.insert()
                 
            return jsonify({
                'success': True
            })
        
        except:
            abort(422)   
    
    # POST actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        new_movie_id = body.get('movie_id', None)

        try:
            actor = Actor(name=new_name, age=new_age, gender=new_gender, movie_id=new_movie_id)
            actor.insert()
                 
            return jsonify({
                'success': True
            })
        
        except:
            abort(422)   
    
    # patch movies
    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(payload, id):

        movie = Movie.query.filter(Movie.id == id).one_or_none() 

        if not movie:
            abort(404)

        body = request.get_json()

        title = body.get('title', None)
        release_month = body.get('release_month', None)

        if title:
            movie.title = title
        if release_month:
            movie.release_month = release_month

        movie.update()

        return jsonify({
            "success": True,
            "movie updated": movie.format()
        })

    # patch actors
    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(payload, id):

        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if not actor:
            abort(404)

        body = request.get_json()

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        if name:
            actor.name = name
        if age:
            actor.age = age
        if gender:
            actor.gender = gender

        actor.update()

        return jsonify({
            "success": True,
            "actor updated": actor.format()
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

    return app

app=create_app()