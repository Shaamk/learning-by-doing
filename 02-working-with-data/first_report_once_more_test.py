from movie_data import movies

def main():
    total_number_of_movies()
    average_rating_of_movies()
    best_movie_short_code()
    worst_movie_for_loop()
    movie_lamda()
    best_movie_list_comprehension()



def total_number_of_movies():
    print(f'The total number of movies: {len(movies)}')


def average_rating_of_movies():
    total_rating = 0
    for movie in movies:
        rating = movie["rating"]
        total_rating += rating
    print(f'Average rating of movies: {total_rating / len(movies)}')


def best_movie_short_code():
    best = 0
    for movie in movies:
        if movie['rating'] > best:
            best = movie["rating"]
            film = movie['title']       # dit stukje !
    print(f'The best movie: {film}')
        

def worst_movie_for_loop():
    worst = 10
    for movie in movies:
        if movie["rating"] < worst:
            worst = movie["rating"]
    for movie in movies:
        if movie["rating"] == worst:
            print(f'The worst movie: {movie["title"]}')


def movie_lamda():
    print()
    best = max(movies, key=lambda x:x["rating"])
    print(f'The LAMBDA best movie: {best["title"]}')
    worst = min(movies, key=lambda x:x["rating"])
    print(f'The LAMBDA worst movie: {worst["title"]}')
    print()


def best_movie_list_comprehension():
    rating = [x['rating'] for x in movies]
    print(max(rating))
    print(min(rating))
    best = max(rating)
    print(best)
    worst = min(rating)
    print(worst)

    min_rating = min(movie['rating'] for movie in movies)
    print(min_rating)



if __name__ == '__main__':
    main()
