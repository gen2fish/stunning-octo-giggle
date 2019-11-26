# stunning-octo-giggle

Movie Database and API Exersice

## Authentication

- HTTP Basic Authentication

## Endpoints

### /movie

- GET - Get all movies in the database
  - Optional query string, sort ascending
    - http://localhost/api/movie?sort=rating

### /movie/[id]

- GET - Get a movie by ID
- POST - Insert new movie into the database
- PUT - Edit Existing Movie
- DEL - Remove movie from database

### Movie Object

```json
{
"title": "Test5",
"format": "VHS",
"rating": 3,
"releaseYear": 1980
}
```
