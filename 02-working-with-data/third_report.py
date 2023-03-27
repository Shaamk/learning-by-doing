# Matthew Broderick     in movie: movie -1
# Judd Nelson           in movie: movie += 1
# Coplayers in movie: movie += 1
# What is the best movie of Ally Sheedy: ?


from movie_data import movies

def main():
    the_first_movies_dict = movies_actors_list()
    the_second_movies_dict = movies_ratings_list()
    matthew_broderick_score(the_first_movies_dict, the_second_movies_dict)
    the_judd_nelson_movies_list, judd_nelson = judd_nelson_score(the_first_movies_dict)
    updated_co_players_list = co_players_of_judd_nelson_movies(the_judd_nelson_movies_list, the_first_movies_dict, judd_nelson)
    movies_one_point_better(updated_co_players_list, the_first_movies_dict, the_second_movies_dict)
    ally_sheedy_best(the_first_movies_dict, the_second_movies_dict)


def movies_actors_list():
    the_first_movies_dict = {}
    for movie in movies:
        title = movie["title"]
        actors = movie["actors"]
        the_first_movies_dict[title] = actors
    return the_first_movies_dict


def movies_ratings_list():
    the_second_movies_dict = {}
    for movie in movies:
        title = movie["title"]
        rating = movie["rating"]
        the_second_movies_dict[title] = rating
    return the_second_movies_dict
    
    
def matthew_broderick_score(the_first_movies_dict, the_second_movies_dict):
    matthew_broderick = 'Matthew Broderick'
    the_matthew_broderick_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if matthew_broderick in list_of_actors]
    for keys in the_matthew_broderick_movies_list:
        if keys in the_second_movies_dict:
            the_second_movies_dict[keys] = the_second_movies_dict[keys] - 1


def judd_nelson_score(the_first_movies_dict):
    judd_nelson = 'Judd Nelson'
    the_judd_nelson_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if judd_nelson in list_of_actors]
    return the_judd_nelson_movies_list, judd_nelson


def co_players_of_judd_nelson_movies(the_judd_nelson_movies_list, the_first_movies_dict, judd_nelson):
    co_players_of_judd_nelson_list = []
    for title in the_judd_nelson_movies_list:
        co_players_of_judd_nelson_list.extend(the_first_movies_dict[title])    
    updated_co_players_list = []
    for player in co_players_of_judd_nelson_list:
        if player not in updated_co_players_list and player != judd_nelson:
            updated_co_players_list.append(player)
    return updated_co_players_list
    
   
def movies_one_point_better(updated_co_players_list, the_first_movies_dict, the_second_movies_dict):
    movies_of_co_players_list = []
    for co_player in updated_co_players_list:
        for title, list_of_actors in the_first_movies_dict.items():
            if co_player in list_of_actors and title not in movies_of_co_players_list:
                movies_of_co_players_list.append(title)    
    for keys in movies_of_co_players_list:
        if keys in the_second_movies_dict:
            the_second_movies_dict[keys] = the_second_movies_dict[keys] + 1


def ally_sheedy_best(the_first_movies_dict, the_second_movies_dict):
    ally_sheedy = 'Ally Sheedy'
    the_ally_sheedy_movies_list = [title for title, list_of_actors in the_first_movies_dict.items() if ally_sheedy in list_of_actors]  
    best_ally_sheedy_rating = 0
    for best_ally_movie in the_ally_sheedy_movies_list:
        for title, rating in the_second_movies_dict.items():
            if best_ally_movie in title and rating > best_ally_sheedy_rating:
                ally = title
    print(f"The best Ally Sheedy movie: {ally}")
            



if __name__ == '__main__':
    main()