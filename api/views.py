from flask import Blueprint, jsonify, request
from . import db
from .models import Movie

main = Blueprint('main', __name__)

@main.route('/movies', methods=['POST'])
def add_entry():
    movie_data = request.get_json()
    new_movie = Movie(
    title=movie_data['title'],
    rating=movie_data['rating'],
    genre=movie_data['genre'],
    release=movie_data['release'],
    image=movie_data['image'],
    created=movie_data['created'],
    description=movie_data['description'])
    db.session.add(new_movie)
    db.session.commit()
    return 'done', 201

@main.route('/movies', methods=['GET'])
def return_entry():
    movie_list = Movie.query.all()
    movies = []
    for movie in movie_list:
        movies.append({'title' : movie.title, 'rating' : movie.rating, 'description': movie.description})

    return jsonify({'movies' : movies})

@main.route('/movies/<int:id>', methods=['DELETE'])
def delete(id):
    movies = Movie.query.get_or_404(id)
    db.session.delete(movies)
    db.session.commit()
    return 'done', 192