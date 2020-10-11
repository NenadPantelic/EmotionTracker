# Movie recommendation API

Movie recommendation API operates as a recommendation API that based on the provided emotion recommends movies of some genre. 


## Dataset 

It internally uses IMDB dataset and recommends top IMDB movies. To setup recommendation API, IMDB dataset must be downloaded. Cleaned IMDB dataset in csv format can be found [`here`](https://drive.google.com/file/d/1Sb6UVwp6HYb7huo74Kbf-XDqQsM334rV/view?usp=sharing). To use it properly, place it into the ***data*** directory -  data/movies.csv. Dataset contains data for more than 85k IMDB movies.

## Installation 

API uses sqlite DBMS, so make sure you install it. API is developed with the Flask framework. Dependencies can be found in requirements.txt file and can be downloaded from PyPi.
```python
pip install <dependency_module>
```
The easier way to install them is to let pip install all the requirements modules on itself:
```python
pip install -r requirements.txt
```

Another option is to use toml poetry config file to install all dependencies:
```python
poetry install
```
  

## Usage

First of all database must be created and populated. In order to do that use the following script:
```python
python3 load_db.py
```
This initial database dumping can take a while (to insert more than 85k records).
After you've loaded the database and installed all the requirement modules, you can run the recommendation API server.
```python
python3 main.py
```
Server will go live on port 8000.

## Endoints

The only avaiable endpoints is the recommendation endpoint with the given URL: /api/v1/recommend
HTTP method: POST
Consumes: application/json
Produces: application/json
Request body:
```json
{
   "emotion": "emotion that should determine genre of the recommended movies",
   "num_of_movies":5,
   "recommendation_type":"type of recommendation you want"
    
}
```
Request body parameters description:
- *emotion* - type := string ; possible values := {"Angry","Disguist", "Fear", "Happy", "Sad","Fantasy", "Neutral"}
- *num_of_movies* - type := int (positive) e.g. 10
- *recommendation_type* - type := string; possible values := {"improve", "keepup"}

## Example

- Request example:
```curl
curl --location --request POST 'localhost:8000/api/v1/recommend' --header 'Content-Type: application/json' --data-raw '{"emotion": "Happy", "num_of_movies": 3, "recommendation_type": "improve"}'
```
- Response example:
```json
{
    "movies": [
        {
            "actors": "Ron Moody, Mike Reid, Miles Petit, Danny Ogle, Jason Gerard, Helena Roman, Matthew Hendrickson, Spyros Merianos, Abbie Balchin, Rachel Balchin, Jason Bullet, Ernesto Cantu, Andy Cheeseman, Emily Corcoran, Lynette Creane",
            "description": "Getaway driver Miles Foster is placed in witness protection after the murder of his friend Andres by Astin Brody, a shady underworld boss. Miles is hidden on the Greek Island of Zanthi with...",
            "directors": "Danny Patrick",
            "duration": 90,
            "genre_name": "Adventure",
            "imdb_url": "https://www.imdb.com/title/tt0451130/",
            "movie_id": "tt0451130",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BOTUwMmI1MWEtYzRkNy00NjBkLTllM2YtZmNkNmVjODI1M2Q2XkEyXkFqcGdeQXVyMzA2ODY0NA@@.jpg",
            "production_company": "Empire Productions",
            "score": 9.3,
            "title": "Moussaka & Chips",
            "year": 2005
        },
        {
            "actors": "Bryan Cranston, Arun Govil, Edie Mirman, Rael Padamsee, Namrata Sawhney, James Earl Jones, Shatrughan Sinha, Jinder Walia, Amrish Puri, Mishal Varma, Tom Wyner, Richard Cansino, Shakti Singh, Dilip Sinha, Michael Sorich",
            "description": "An anime adaptation of the Hindu epic the Ramayana, where Lord Ram combats the wicked king Ravana.",
            "directors": "Ram Mohan, Yûgô Sakô",
            "duration": 170,
            "genre_name": "Adventure",
            "imdb_url": "https://www.imdb.com/title/tt0259534/",
            "movie_id": "tt0259534",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BOTk4NGM0NmUtOTc2Yi00NTcxLWE3NGItYzEwODZjNzlhZjE2XkEyXkFqcGdeQXVyNTgyNTA4MjM@.jpg",
            "production_company": "Nippon Ramayana Film Co.",
            "score": 9,
            "title": "Ramayana: The Legend of Prince Rama",
            "year": 1992
        },
        {
            "actors": "",
            "description": "",
            "directors": "Yukio Kaizawa",
            "duration": 70,
            "genre_name": "Adventure",
            "imdb_url": "https://www.imdb.com/title/tt10037700/",
            "movie_id": "tt10037700",
            "poster_url": "https://m.media-amazon.com/images/M/MV5BYzIyMWRkMTktZmYyYy00YzZkLWFlOWEtOGU2MmEyNjVkZDk3XkEyXkFqcGdeQXVyNzEyMDQ1MDA@.jpg",
            "production_company": "Toei Animation",
            "score": 9,
            "title": "Precure Miracle Universe Movie",
            "year": 2019
        }
    ]
}
```


