# Full Stack Capstone Project

## Getting Started 

Heroku hosted app url: https://capstone-12345.herokuapp.com/ 

## Project Motivations

The Casting Agency is an application to manage a database movies and actors. This is done using a flask application and a postgres database.  

### Dependencies

Some of the required backend packages are:
- flask
- flask-sqlalchemy
- flask-cors
- unittest

Other dependencies are mentioned in requiremnts.txt

Packages are to be installed using pip.

```
pip install package
```

```
pip install -r requirements.txt
```

### Running Locally

From the project folder, run the following commands to start the application:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Base URL: http://127.0.0.1:5000/

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```
Error types returned when requests fail are:

- 404: Resource Not Found
- 422: Not Processable
- 405: Method Not Allowed
- 400: Bad Request

## Endpoints

### GET '/movies'

- Returns the list of movies.
- Request Arguments: None
- Returns: An object with all the movies containing their titles and release months.

```
{
    "title":"batman",
    "release_month":"may"
}
```

### POST '/movies'

- Sends a post request in order to add a new movie
- Request Body:

```
{
    "title":"superman",
    "release_month":"november"

}
```

- Returns: 

```
{
    "Success":"true"
}
```

### DELETE '/movies/<int:id>'

- Deletes a specified movie using the id of the movie
- Request Arguments: id - integer
- Returns: 

```
{
    "Success":"true"
}
```

### PATCH '/movies/<int:id>'

- Sends a patch request in order to update a movie
- Request Body:

```
{
    "release_month":"january"

}
```

- Returns: 

```
{
    "Success":"true",
    "updated_movie":
    {
        "title":"batman",
        "release_month":"january"
    }
}
```

### GET '/actors'

- Returns the list of actors.
- Request Arguments: None
- Returns: An object with all the movies containing their names, ages and genders.

```
{
    "name":"david",
    "age":23,
    "gender":"male"
}
```

### POST '/movies'

- Sends a post request in order to add a new actor
- Request Body:

```
{
    "name":"ben",
    "age":29,
    "gender":"male"

}
```

- Returns: 

```
{
    "Success":"true"
}
```

### DELETE '/actors/<int:id>'

- Deletes a specified actor using the id of the actor
- Request Arguments: id - integer
- Returns: 

```
{
    "Success":"true"
}
```

### PATCH '/actors/<int:id>'

- Sends a patch request in order to update an actor
- Request Body:

```
{
    "age":24

}
```

- Returns: 

```
{
    "Success":"true",
    "updated_actor":
    {
        "name":"david",
        "age":24
        "gender":"male"
    }
}
```

## RBAC

### Roles

There are three roles present in the project.

1) Agent

- Can view actors and movies

2) Director

- All permissions an agent has and…
- Add or delete an actor from the database
- Modify actors or movies

3) Producer

- All permissions a director has and…
- Add or delete a movie from the database

### Access Tokens

The endpoints can be accessed using the following bearer tokens as the header

- Agent: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4MmYzNzU5NWU0Yzk5NTY4NTE3IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0Mjg5OCwiZXhwIjoxNjY5MzI5Mjk4LCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.U0LRRnRev2H54x50PW4c9xoNeikw8xEqYu8R0mXOT_CQwSktsEyEA95rB6pl7y6er1gfEbWrokrtHt6rtvKevyRc4N0QgrUySrUPQ7U-EGzacMnnrm9uAhQEYAtFiNDrZQ5cEWzMPkXPYVmkpcaPIj9ekxsInu7vNY1QKmE5mZIojkAAJfqIFfv86XJRVDKH28pl3xFeGWEG53IrhBjGFAEX8ey0MPp_SmIcmm3uukkn9EumM0AP3DCd-Vz4b5EwogqAZNNCR4hf-bQuKhM5g8e58wKYSM_bbLakmNA2l368QlpstKRVdNIojjTxf64gUZ0dC37LO3TgPZFuLs2smg

- Director: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4NjJjMGY4YWFiZmY2NGE2YTEyIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0MjczNCwiZXhwIjoxNjY5MzI5MTM0LCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.hpb0hHco2BH9peds7DCvZptn3yv8CkOxfRDRUHEYrXzATGBxwwZAibKR3mHiaOqnpbaTLi4Shb4mgHO6MoyhUaxADJBQE3wUIgvnuXgxgLujOdhYlAaOJf1gzyaCZipsFc9hvbBlNcH7Vpr0QimwV6gidqyTuzoyMzwq-J77Hn4TzSLuuFLvwAGWYHt2tn7vT12TG5CdC4nOmeQcZAWCvKonQy89vn0vxMeLTgZREZHkkw27URiN-acPqFbz40VA8bOu35UOWsNsBzoEWXJ383I3EXy5g0Iuk1vGxUYXt-0RikyBtF-XBvLChm5CYvyV4pfQPTjz_amaX3INw005Ug

- Producer: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdTTUUwazJkZFp0blYtdEVoNUNQbCJ9.eyJpc3MiOiJodHRwczovL2Rldi13eHRyczQzcC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjM3Y2Y4ODljM2NmZWQ2NzhhYzBlYmZhIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY2OTI0MzM4MiwiZXhwIjoxNjY5MzI5NzgyLCJhenAiOiJtR2xQT0JBTzlKWUZZZ3c1aGdOMzdWQUhQeU9meGhuYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Cy7pNkKNczMwacs2Q8O4EOZ-avw90YfBWFLr6rgdqeDNMr7DaDlOfwd2SAJyr4ij6srZWyHJuw86QbrVa56kbcu6UM5oQsKxkeEtxkSeNmNWZRVIKUbzdEF3YRXQc5K3xvihVZ2QHlfz2EzW46Y4PE3ZhQ4qOzi4jk6TMx_ylWZyLXNOEZuOd4gOL1p1B-Csnsx0HiQaly4fnpOHcAThJf7hhBk39kzpeXcjkr7xU3ea6xVf2betgKwTLYGOkULzuwj4u9zg1-689fcGlhbPUodRZswJ-F6r0KSHyMpxa5TVr1oPIZQjKLqXWvjqOpbMGbw49qwOwm1rrblkCjBv9Q