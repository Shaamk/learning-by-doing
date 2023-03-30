# List : List the name and year of all movies, separated by a comma.
# Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
# Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
# Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
# Quit : Ends the program.

from movie_data import movies


def main():
    options_to_choose()


def options_to_choose():
    option = True
    while option:
        print("-"*20)
        print("1. List\n2. Actor search\n3. Genre search\n4. Adding a new movie\n5. End program")
        print("-"*20)
        option = input("select your option: ")
        if option == "1":            
            movies_list()
        elif option == "2":
            actor_search()
        elif option == "3":
            genre_search()
        elif option == "4":
            adding_movie()
        elif option == "5":
            # Quit : Ends the program.
            print("Ending")
            option = False

    
# List : List the name and year of all movies, separated by a comma.
def movies_list():
    for movie in movies:
        print(f'{movie["title"]}, {movie["year"]}')


# Actor Search : Prompt for an actor's name, then list the "title" and "year" of all their movies.
def actor_search():
    actor_string = input("What is the name of the actor ?: ")
    for movie in movies:
        if actor_string in movie["actors"]:
            print(f'{movie["title"]}, {movie["year"]}')
    

# Genre Search : Prompt for a genre name, then list the "title" and "year" of every movie in that genre.
def genre_search():
    genre_string = input("What genre are you looking for ?: ")
    for movie in movies:
        if genre_string in movie["genre"]:
            print(f'{movie["title"]}, {movie["year"]}')


# Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
def adding_movie():
    print("Please add your new movie: ")
    add_movie = []
    new_movie = {}
    new_movie["title"] = input("title: ")
    new_movie["actors"] = [input("actors: ")]
    new_movie["year"] = input("year: ")
    new_movie["genre"] = input("genre: ")
    new_movie["rating"] = input("rating: ")
    add_movie.append(new_movie)
    print(add_movie)
    movies.append(add_movie)
    print(movies)


if __name__ == '__main__':
    main()
