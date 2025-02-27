from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

movies = [
    {'id': 1, 'title': 'Movie 1', 'description': 'Description of Movie 1'},
    {'id': 2, 'title': 'Movie 2', 'description': 'Description of Movie 2'},
    {'id': 3, 'title': 'Movie 3', 'description': 'Description of Movie 3'}
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:id>')
def movie(id):
    movie = next((m for m in movies if m['id'] == id), None)
    if movie is None:
        return "Movie not found", 404
    return render_template('movie.html', movie=movie)

@app.route('/random')
def random_movie():
    movie = random.choice(movies)
    return redirect(url_for('movie', id=movie['id']))

if __name__ == '__main__':
    app.run(debug=True)
