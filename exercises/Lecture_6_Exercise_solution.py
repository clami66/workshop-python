#!/usr/bin/env python

from sys import argv

def format_sec(seconds):   # input a list of seconds, output is a string
    hours     = int(seconds/3600)
    minutes   = int((seconds - (3600*hours))/60)
    #return str(hours)+"h"+str(round(minutes))+"min"
    return f"{hours}h {minutes}min"

def format_output(movie_rating, movie_title, movie_year, movie_runtime):
    return f"{movie_rating}\t{movie_title} ({movie_year}) [{movie_runtime}]\n"

# run as e.g.: python imdb_restructure_solution.py 250.imdb 250_restructured.imdb
input_file = argv[1]
output_file = argv[2]

movies = open(input_file, "r")
movies_by_genre = {} # movies_by_genre["drama"] -> [movie1, movie2, movie3]

for movie in movies:
    if not movie.startswith("#"):
        movie = movie.strip()
        movie_split = movie.split("|")
        ranking = float(movie_split[1])
        year = movie_split[2]
        runtime = int(movie_split[3])
        genres = movie_split[5]
        title = movie_split[6]
        
        for genre in genres.split(","):
            genre = genre.lower()
            if genre not in movies_by_genre:
                # initialize a list containing one element (tuple)
                movies_by_genre[genre] = [(ranking, title, year, runtime)]
            else:
                # append more tuples to the list for that genre
                movies_by_genre[genre].append((ranking, title, year, runtime))

movies.close()

reformat = open(output_file, "w")
for genre in movies_by_genre:
    reformat.write(f"> {genre}\n")
    movies_for_this_genre = movies_by_genre[genre]
    for movie in movies_for_this_genre:
        runtime = format_sec(movie[3])
        reformat.write(format_output(movie[0], movie[1], movie[2], format_sec(movie[3])))
        
reformat.close()
