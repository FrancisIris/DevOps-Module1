from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/films/list')
def list_of_films():
    return render_template("list.html")

@app.route('/films')
def get_films():
    return render_template('film_list.html',films=makeFilmsList())

@app.route('/films/table')
def show_input_as_table():
    stars=request.values.get("stars", "")
    filmList=makeFilmsList()
    filmList=(film for film in filmList if int(stars) ==int(film[1]))
    return render_template('film_list.html',films=filmList)


@app.route("/show-message")
def echo():
    name = request.values.get("name", "")
    message = request.values.get("message", "")

    return f"Hey there {name}! you said {message}"

def makeFilmsList():
    filmsDoc = open("films.txt", "r").read().splitlines()
    films=[]
    for line in filmsDoc:
        line=line.split(",")
        line[1]=int(line[1])
        films.append(line)
    return films