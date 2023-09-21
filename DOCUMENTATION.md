
# API Documentation
​A Token Authenticated API for performing GET and POST operations on PERSON and MOVIE resource. By simply providing the username and password of the user to generate a Bearer token, and by specifying the corresponding HTTP requests, you can create and retrieve movie records.
### API Endpoints
#### Using the API
​
The API provides the following endpoints for managing persons and movie:
​
- POST `/api/signup` : Create a new person, and generate a token.
- GET `/api/movie` : Get person by their ID.
- POST `/api/movie` : create a new Movie.
​
#### Standard Request and Response Formats
​
- For the `POST /api/signup`endpoint, send a JSON request body with the username and password field.
- For the `POST /api/movie`endpoint, send a JSON request body with the title, protagonist, description, series_or_movie, genre and rating field.
- For the `GET /api/movie` endpoint, you would receive a JSON response with the details of the movies in the database.
​
#### Create a New User(Signup) and generate Token
```
curl -X 'POST' \
 'http://127.0.0.1:8000/api/signup' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -d '{
 "username": "Peter Drury",
 "password": "peter"
}' 
```

- **Request Format**
```
    {
        "username": "Peter Drury",
        "password": "123456"
   }
```
​
- **Response Format:**
  ```
  {
        "username": "Peter Drury",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYmVhcmVyIiwiZXhwIjoxNjk1MzE2MDE3LCJpYXQiOjE2OTUzMTQyMTcsInN1YiI6IlBldGVyIERydXJ5In0",
        "token_type": "bearer"
  }
  ```
​
#### Get all Movie
##### `Authorisation: Bearer <token>`
##### `Token used in this documentation is not valid, the tokens will expire after 30 minute`
​
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/movie' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYmVhcmVyIiwiZXhwIjoxNjk1MzE2MTYyLCJpYXQiOjE2OTUzMTQzNjIsInN1YiI6IlBldGVyIERydXJ5In0'
```

- **Response Format:**
  ```
  [
        {
          "title": "Grimm",
          "protagonist": "Nick Burkhardt",
          "description": "Dive into the supernatural, as HE kills Wesen that terrorizes humans, HE defends, protects and save his family",
          "series_or_movie": "series",
          "genre": "Sci-fi, action",
          "rating": 7
        },
        {
          "title": "Fast and Furious",
          "protagonist": "Vin Diesel",
          "description": "Fast, Steady, Professional, impossible, Slow and Steady doesn't win the race, HE defends, protects and save his family",
          "series_or_movie": "Movie",
          "genre": "Sci-fi, action, adventure",
          "rating": 8
        },
  ]

#### Add a Movie to the DB
##### `Authorisation: Bearer <token>`
```
    curl -X 'POST' \
    'http://127.0.0.1:8000/api/movie' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYmVhcmVyIiwiZXhwIjoxNjk1MzE2MTYyLCJpYXQiOjE2OTUzMTQzNjIsInN1YiI6IlBldGVyIERydXJ5In0.' \
    -H 'Content-Type: application/json' \
    -d '  {
              "title": "Jumanji",
              "protagonist": "Kevin Hart, DeRock",
              "description": "Adventures of all a lifetime, explore the depth of the jungle,'\''through the screen'\'' NOPE...Inside the screen!!!",
              "series_or_movie": "Movie",
              "genre": "Sci-fi, action, adventure",
              "rating": 8
          }
```

- **Request Format:**

  ```
  {
      "title": "Jumanji",
      "protagonist": "Kevin Hart, DeRock",
      "description": "Adventures of all a lifetime, explore the depth of the jungle,'through the screen' NOPE...Inside the screen",
      "series_or_movie": "Movie",
      "genre": "Sci-fi, action, adventure",
      "rating": 8
  }

- **Response Format:**

```
{
  "title": "Jumanji",
  "protagonist": "Kevin Hart, DeRock",
  "description": "Adventures of all a lifetime, explore the depth of the jungle,'through the screen' NOPE...Inside the screen",
  "series_or_movie": "Movie",
  "genre": "Sci-fi, action, adventure",
  "rating": 8
}
```
​
## Local Setup and Deployment
​
- Clone the repository and follow the installation steps mentioned in the `README.md`` file.
- Start the API by `uvicorn main:app --reload`.
- The API will be available at http://127.0.0.1:8000/. 

