# Total number of movies: 231
# Average rating of movies: 2.7
# Best movie: "2 Fast 2 Furios"
# Worst movie: "Citizen Kane"


from movie_data import movies


def main():
    total = total_movies()
    average_rating(total)
    best_movie()
    worst_movie()
    
    
def total_movies():
    total = len(movies)
    print(f"Total number of movies: {total}")
    return total


def average_rating(total):
    sum = 0
    for movie in movies:
        rating = movie["rating"]
        sum += rating
    average = sum / total
    print(f"Average rating of movies: {average}")
    
         
def best_rating():
    highest_rating = 0
    for movie in movies:
        rating = movie["rating"]
        if rating > highest_rating:
            highest_rating = rating
    return highest_rating


def worst_rating():
    lowest_rating = 10
    for movie in movies:
        rating = movie["rating"]
        if rating < lowest_rating:
            lowest_rating = rating
    return lowest_rating            


def best_movie():
    highest_rating = best_rating()
    for movie in movies:
        if highest_rating == movie["rating"]:
            best = movie["title"]
            print(f"Best movie: {best}")


def worst_movie():
    lowest_rating = worst_rating()
    for movie in movies:
        if lowest_rating == movie["rating"]:
            worst = movie["title"]
            print(f"Worst movie: {worst}")


if __name__ == "__main__":
    main()
