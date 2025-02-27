from flask import Flask, render_template, redirect, url_for, abort
import random

app = Flask(__name__)

movies = [
    {'id': 1, 'title': 'Inception', 'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the task of planting an idea into the mind of a CEO.'},
    {'id': 2, 'title': 'The Matrix', 'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'},
    {'id': 3, 'title': 'The Dark Knight', 'description': 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'},
    {'id': 4, 'title': 'Interstellar', 'description': 'A team of explorers must find a new planet for humanity as Earth’s resources are dwindling and the planet is dying.'},
    {'id': 5, 'title': 'The Shawshank Redemption', 'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'},
    {'id': 6, 'title': 'Forrest Gump', 'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal, and other historical events unfold from the perspective of an Alabama man with an extraordinary life.'},
    {'id': 7, 'title': 'Pulp Fiction', 'description': 'The lives of two mob hitmen, a boxer, a gangster’s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'},
    {'id': 8, 'title': 'Gladiator', 'description': 'A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family and sent him into slavery.'},
    {'id': 9, 'title': 'Fight Club', 'description': 'An insomniac office worker and a soap salesman form an underground fight club that evolves into something much, much more.'},
    {'id': 10, 'title': 'The Godfather', 'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'}
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:id>')
def movie(id):
    movie = next((m for m in movies if m['id'] == id), None)
    if movie is None:
        abort(404)
    return render_template('movie.html', movie=movie)

@app.route('/random')
def random_movie():
    random_movie = random.choice(movies)
    return redirect(url_for('movie', id=random_movie['id']))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
