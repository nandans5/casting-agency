import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *


class CapstoneTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres', 'localhost:5433', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
            'name':'John',
            'age':30,
            'gender':'male'
        }

        self.new_actor2 = {
            'name':'Sarah',
            'age':28,
            'gender':'female'
        }

        self.new_movie = {
            'title':'Ironman',
            'release_month':'may',
        }

        self.new_movie2 = {
            'title':'Superman',
            'release_month':'november',
        }

        self.patch_movie = {
            'title':'Batman'
        }

        self.patch_actor = {
            'name':'George'
        }

        self.agent_auth = {'Authorization':'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4MmYzNzU5NWU0Yzk5NTY4NTE3IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0Mjg5OCwiZXhwIjoxNjY5MzI5Mjk4LCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.U0LRRnRev2H54x50PW4c9xoNeikw8xEqYu8R0mXOT_CQwSktsEyEA95rB6pl7y6er1gfEbWrokrtHt6rtvKevyRc4N0QgrUySrUPQ7U-EGzacMnnrm9uAhQEYAtFiNDrZQ5cEWzMPkXPYVmkpcaPIj9ekxsInu7vNY1QKmE5mZIojkAAJfqIFfv86XJRVDKH28pl3xFeGWEG53IrhBjGFAEX8ey0MPp_SmIcmm3uukkn9EumM0AP3DCd-Vz4b5EwogqAZNNCR4hf-bQuKhM5g8e58wKYSM_bbLakmNA2l368QlpstKRVdNIojjTxf64gUZ0dC37LO3TgPZFuLs2smg'}
        self.director_auth = {'Authorization':'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4NjJjMGY4YWFiZmY2NGE2YTEyIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0MjczNCwiZXhwIjoxNjY5MzI5MTM0LCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.hpb0hHco2BH9peds7DCvZptn3yv8CkOxfRDRUHEYrXzATGBxwwZAibKR3mHiaOqnpbaTLi4Shb4mgHO6MoyhUaxADJBQE3wUIgvnuXgxgLujOdhYlAaOJf1gzyaCZipsFc9hvbBlNcH7Vpr0QimwV6gidqyTuzoyMzwq-J77Hn4TzSLuuFLvwAGWYHt2tn7vT12TG5CdC4nOmeQcZAWCvKonQy89vn0vxMeLTgZREZHkkw27URiN-acPqFbz40VA8bOu35UOWsNsBzoEWXJ383I3EXy5g0Iuk1vGxUYXt-0RikyBtF-XBvLChm5CYvyV4pfQPTjz_amaX3INw005Ug'}
        self.producer_auth = {'Authorization':'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4ODljM2NmZWQ2NzhhYzBlYmZhIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0MzM4MiwiZXhwIjoxNjY5MzI5NzgyLCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Cy7pNkKNczMwacs2Q8O4EOZ-avw90YfBWFLr6rgdqeDNMr7DaDlOfwd2SAJyr4ij6srZWyHJuw86QbrVa56kbcu6UM5oQsKxkeEtxkSeNmNWZRVIKUbzdEF3YRXQc5K3xvihVZ2QHlfz2EzW46Y4PE3ZhQ4qOzi4jk6TMx_ylWZyLXNOEZuOd4gOL1p1B-Csnsx0HiQaly4fnpOHcAThJf7hhBk39kzpeXcjkr7xU3ea6xVf2betgKwTLYGOkULzuwj4u9zg1-689fcGlhbPUodRZswJ-F6r0KSHyMpxa5TVr1oPIZQjKLqXWvjqOpbMGbw49qwOwm1rrblkCjBv9Q'}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_get_not_valid(self):
        res = self.client().get('/movies/1000', headers=self.producer_auth)

        self.assertEqual(res.status_code, 405)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_create_new_movie2(self):
        res = self.client().post('/movies', json=self.new_movie2, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie2, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_create_movie_not_allowed(self):
        res = self.client().post('/movies/100', json=self.new_movie, headers=self.producer_auth)

        self.assertEqual(res.status_code, 405)
    
    def test_patch_movie(self):
        res = self.client().patch('/movies/2', json=self.patch_movie, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_patch_movie_not_allowed(self):
        res = self.client().patch('/movies/100', json=self.patch_movie, headers=self.producer_auth)

        self.assertEqual(res.status_code, 404)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers=self.producer_auth)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)

    def test_422_if_movie_does_not_exist(self):
        res = self.client().delete('/movies/1000', headers=self.producer_auth)

        self.assertEqual(res.status_code, 422)
        
    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_get_not_valid_actors(self):
        res = self.client().get('/actors/1000', headers=self.producer_auth)

        self.assertEqual(res.status_code, 405)

    def test_create_new_actor(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_create_new_actor2(self):
        res = self.client().post('/actors', json=self.new_actor2, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_create_actor_not_allowed(self):
        res = self.client().post('/actors/100', json=self.new_actor, headers=self.producer_auth)

        self.assertEqual(res.status_code, 405)
    
    def test_patch_actor(self):
        res = self.client().patch('/actors/2', json=self.patch_actor, headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)

    def test_patch_actor_not_allowed(self):
        res = self.client().patch('/actors/100', json=self.patch_actor, headers=self.producer_auth)

        self.assertEqual(res.status_code, 404)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.producer_auth)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)

    def test_422_if_actor_does_not_exist(self):
        res = self.client().delete('/actors/1000', headers=self.producer_auth)

        self.assertEqual(res.status_code, 422)


    # RBAC test

    # agent
    def test_delete_movie_agent(self):
        res = self.client().delete('/movies/1', headers=self.agent_auth)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(res.status_code, 403)

    def test_delete_actor_agent(self):
        res = self.client().delete('/actors/1', headers=self.agent_auth)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(res.status_code, 403)
    
    def test_get_movies_agent(self):
        res = self.client().get('/movies', headers=self.agent_auth)

        self.assertEqual(res.status_code, 200)

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.producer_auth)

        self.assertEqual(res.status_code, 200)



    # director

    def test_delete_movie_director(self):
        res = self.client().delete('/movies/2', headers=self.director_auth)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 403)

    def test_create_new_movie_director(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.director_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_get_movies_director(self):
        res = self.client().get('/movies', headers=self.director_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.director_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()