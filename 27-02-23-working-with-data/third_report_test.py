# Matthew Broderick     in movie: movie -1
# Judd Nelson           in movie: movie += 1
# Coplayers in movie: movie += 1
# What is the best movie of Ally Sheedy: ?


from movie_data import movies

def main():
    movies_list()



def movies_list():
    the_first_movies_dict = {}
    for movie in movies:
        title = movie["title"]
        actors = movie["actors"]
        the_first_movies_dict[title] = actors
    print(the_first_movies_dict)                # prints titles with actors in a dictionary
    print()


    the_second_movies_dict = {}
    for movie in movies:
        title = movie["title"]
        rating = movie["rating"]
        the_second_movies_dict[title] = rating
    print(the_second_movies_dict)               # prints titles with ratings in a dictionary
    print()
    

    matthew_broderick = 'Matthew Broderick'
    the_matthew_broderick_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if matthew_broderick in list_of_actors]
    print(f"Matthew Brodericks movies: {the_matthew_broderick_movies_list}")
    for keys in the_matthew_broderick_movies_list:          # keys can not be changed into title
        if keys in the_second_movies_dict:                  # keys can not be changed into title
            the_second_movies_dict[keys] = the_second_movies_dict[keys] - 1
    print()
    print(f'Matthew Broderick score: {the_second_movies_dict}')     # prints the score after making the movie worse in a dictionary



    judd_nelson = 'Judd Nelson'
    the_judd_nelson_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if judd_nelson in list_of_actors]
    print()
    print(f"Judd Nelson movies: {the_judd_nelson_movies_list}")
    # for keys in the_judd_nelson_movies_list:
    #     if keys in the_second_movies_dict:
    #         the_second_movies_dict[keys] = the_second_movies_dict[keys] + 1
    # print()
    # print(f'Judd Nelson score: {the_second_movies_dict}')       # prints the score after making the movie better in a dictionay
    # I can also make a score after I get all the names of the movies
    print()


    co_players_of_judd_nelson_list = []
    for title in the_judd_nelson_movies_list:
        co_players_of_judd_nelson_list.extend(the_first_movies_dict[title])            
    print(co_players_of_judd_nelson_list)                   # prints a list of co-players and with "Judd Nelson"
    print()
    

    updated_co_players_list = []
    for player in co_players_of_judd_nelson_list:           # removed Judd Nelson appearing 3 times
        if player not in updated_co_players_list and player != judd_nelson:
            updated_co_players_list.append(player)
    #print(updated_co_players_list)
    print()


    # movies_of_co_players_list = [title for title, list_of_actors in the_first_movies_dict.items() if updated_co_players in list_of_actors]
    # print(movies_of_co_players_list)      
    # list in list is not iterable!

    
    movies_of_co_players_list = []
    for co_player in updated_co_players_list:
        for title, list_of_actors in the_first_movies_dict.items():
            if co_player in list_of_actors and title not in movies_of_co_players_list:
                movies_of_co_players_list.append(title)
    print(f"Movies for one point better:{movies_of_co_players_list}")
    print()

    for keys in movies_of_co_players_list:
        if keys in the_second_movies_dict:
            the_second_movies_dict[keys] = the_second_movies_dict[keys] + 1
    print(f"Every other movie in one point better: {the_second_movies_dict}")
    print()



    ally_sheedy = 'Ally Sheedy'
    the_ally_sheedy_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if ally_sheedy in list_of_actors]
    print(f"Ally Sheedy movies: {the_ally_sheedy_movies_list}")

    
    best_ally_sheedy_rating = 0
    for best_ally_movie in the_ally_sheedy_movies_list:
        for title, rating in the_second_movies_dict.items():
            if best_ally_movie in title and rating > best_ally_sheedy_rating:
                ally = title
    print(f"The best Ally Sheedy movie: {ally}")
            



if __name__ == '__main__':
    main()