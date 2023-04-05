from movie_data import movies

def main():
    total_number_of_movies()
    average_rating_of_movies()
    the_best_movie()
    the_worst_movie()


def total_number_of_movies():
    print(f'The total number of movies: {len(movies)}')


def average_rating_of_movies():
    total_rating = 0
    for movie in movies:
        rating = movie["rating"]
        total_rating += rating
    print(f'Average rating of movies: {total_rating / len(movies)}')


def the_best_movie():
    best = 0
    for movie in movies:
        if movie['rating'] > best:
            best = movie["rating"]
            film = movie['title']       # dit stukje !
    print(f'The best movie: {film}')
        

def the_worst_movie():
    worst = 10
    for movie in movies:
        if movie["rating"] < worst:
            worst = movie["rating"]
    for movie in movies:
        if movie["rating"] == worst:
            print(f'The worst movie: {movie["title"]}')


if __name__ == '__main__':
    main()
