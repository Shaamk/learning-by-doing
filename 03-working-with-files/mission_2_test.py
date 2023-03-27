def main():
    data = getting_the_text_data()
    movies_list, backup_movies_list = storing(data)
    database(movies_list)
    the_new_movies_list = added_to_database(backup_movies_list)
    printing_the_new_database(the_new_movies_list)


def getting_the_text_data():
    with open('20-03-23-working-with-files/movie_data.txt', 'rt') as get_the_movies:
        data = get_the_movies.read()
        return data
        #print(movies.read())


def storing(data):
    movies_list = []
    movies_list = data.splitlines()
    backup_movies_list = list(movies_list)
    # print(f"original movies list: {movies_list}")
    # print()
    # print(f"Back up: {backup_movies_list}")
    # print()
    return movies_list, backup_movies_list
    

def database(movies_list):
    final_movies_list = []
    for i in range(len(movies_list)):
        if i % 5 == 0:
            movie = {}
            movie["title"] = movies_list.pop(0)
            movie["actors"] = movies_list.pop(0)
            movie["year"] = movies_list.pop(0)
            movie["genre"] = movies_list.pop(0)
            movie["rating"] = movies_list.pop(0)        
            final_movies_list.append(movie)
    print(final_movies_list)


def added_to_database(backup_movies_list):
    print("\nPlease enter a new movie: ")
    new_movie_list = []
    new_movie_list.insert(0, input("title: "))
    new_movie_list.insert(1, input("actors: "))
    new_movie_list.insert(2, input("year: "))
    new_movie_list.insert(3, input("genre: "))
    new_movie_list.insert(4, input("rating: "))
    the_new_movies_list = backup_movies_list + new_movie_list
    print("\n",the_new_movies_list)
    return the_new_movies_list
  
    

def printing_the_new_database(the_new_movies_list):
    with open('20-03-23-working-with-files/new_movie_data.txt', 'wt') as start_writing:
        for movies in the_new_movies_list:
            start_writing.write(movies)
            start_writing.write('\n')
    


if __name__ == '__main__':
    main()

