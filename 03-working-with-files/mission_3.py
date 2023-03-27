def main():
    data = getting_the_text_data()
    movies_list, movies_edit_list = storing(data)
    the_final_movies_list = database(movies_list)
    updated_movies_list = options_to_choose(the_final_movies_list, movies_edit_list)
    update_database(updated_movies_list)
    printing_the_new_database(the_final_movies_list)
    

def getting_the_text_data():
    with open('20-03-23-working-with-files/movie_data.txt', 'rt') as get_the_movies:
        data = get_the_movies.read()
        return data
        #print(movies.read())


def storing(data):
    movies_list = []
    movies_list = data.splitlines()
    movies_edit_list = list(movies_list)
    return movies_list, movies_edit_list


def database(movies_list):
    the_final_movies_list = []
    for i in range(len(movies_list)):
        if i % 5 == 0:
            movie = {}
            movie["title"] = movies_list.pop(0)
            movie["actors"] = movies_list.pop(0)
            movie["year"] = movies_list.pop(0)
            movie["genre"] = movies_list.pop(0)
            movie["rating"] = movies_list.pop(0)        
            the_final_movies_list.append(movie)
    return the_final_movies_list


def options_to_choose(the_final_movies_list, movies_edit_list):
    show_menu = True
    while show_menu:
        print("-"*20)
        print("1. List the name and year\n2. Actor search\n3. Genre search\n4. Adding a movie\n5. Save the new movies list to a text file\n6. End of program")
        print("-"*20)
        option = input("select option: ")
        if option == "1":            
            name_and_year(the_final_movies_list)
        elif option == "2":
            actor_search(the_final_movies_list)
        elif option == "3":
            genre_search(the_final_movies_list)
        elif option == "4":
            updated_movies_list = adding_to_database(movies_edit_list)
            the_final_movies_list = update_database(updated_movies_list)
        elif option == "5":
            printing_the_new_database(the_final_movies_list)
        elif option == "6":
            print("End of Program")
            show_menu = False


# 1
def name_and_year(the_final_movies_list):
    for every_movie in the_final_movies_list:
        print(f'{every_movie["title"]}, {every_movie["year"]}')


# 2
def actor_search(updated_final_movies_list):
    actor_string = input("What is the name of the actor to search for: ")    
    for movie_dic in updated_final_movies_list:
        if actor_string in movie_dic["actors"]:
            print(f'{movie_dic["title"]}, {movie_dic["year"]}')


# 3
def genre_search(updated_final_movies_list):
    genre_string = input("What is name of the genre to search for: ")    
    for movie_dic in updated_final_movies_list:
        if genre_string in movie_dic["genre"]:
            print(f'{movie_dic["title"]}, {movie_dic["year"]}')


# 4
def adding_to_database(movies_edit_list):
    print("\nPlease enter a new movie:")
    new_movie = []
    new_movie.insert(0, input("title: "))
    new_movie.insert(1, input("actors: "))
    new_movie.insert(2, input("year: "))
    new_movie.insert(3, input("genre: "))
    new_movie.insert(4, input("rating: "))
    updated_movies_list = movies_edit_list + new_movie
        

    second_question = input("do you want to add one more movie? ")
    if second_question == "no":
        return updated_movies_list
    elif second_question == "yes":
        updated_movies_list = adding_to_database(updated_movies_list)
        return updated_movies_list


def update_database(updated_movies_list):
    updated_final_movies_list = []
    for i in range(len(updated_movies_list)):
        if i % 5 == 0:
            movie = {}
            movie["title"] = updated_movies_list.pop(0)
            movie["actors"] = updated_movies_list.pop(0)
            movie["year"] = updated_movies_list.pop(0)
            movie["genre"] = updated_movies_list.pop(0)
            movie["rating"] = updated_movies_list.pop(0)        
            updated_final_movies_list.append(movie)
    return updated_final_movies_list
    

def printing_the_new_database(the_new_movies_list):
    with open('20-03-23-working-with-files/new_movie_data.txt', 'w') as start_writing:
        for movies in the_new_movies_list:
            start_writing.write(movies)
            start_writing.write('\n')



if __name__ == '__main__':
    main()
