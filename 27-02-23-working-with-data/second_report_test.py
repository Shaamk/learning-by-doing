
# Actor appearring in most movies: Julia Roberts
# Actor with best average rating: Jean Claude Van Damme
# Least popular genre in the 1980's: music videos


from movie_data import movies


def main():
    actors_appearing = appearing()
    best_average_rating(actors_appearing)
    least_popular()
            

def appearing():
    actors_appearing = {}
    for movie in movies:
        actors = movie["actors"]            # actors = list
        for actor in actors:
            if actor in actors_appearing:   # actors_appearing = dictionary
                actors_appearing[actor] += 1
            else:
                actors_appearing[actor] = 1
    maximum_appearing = max(actors_appearing, key=actors_appearing.get)
    print(f"\nActor appearing in most movies: {maximum_appearing}\n")
    return actors_appearing


def best_average_rating(actors_appearing):
    rating = "rating"
    actors_rating = {}
    actors_average_rating = {}
    actors_for_average_rating = {}
    for movie in movies:
        actors = movie["actors"]
        for actor in actors:
            if actor in actors_rating:
                actors_rating[actor] += movie[rating]
            else:
                actors_rating[actor] = movie[rating]
        
    for key in actors_rating:
        if key in actors_appearing:
            actors_average_rating[key] = actors_rating[key] / actors_appearing[key]
        
    actors_max = max(actors_average_rating.values())
    for key in actors_average_rating:
        if actors_average_rating[key] == actors_max:
            actors_for_average_rating[key] = actors_average_rating[key]
        
    for keys in actors_for_average_rating:
        print(f"Actors with best average rating: {keys}")


def least_popular():
    genres_list_for_80 = []
    genres_dict_for_80_appearing = {}
    genre_dict_least_popular = {}
    for movie in movies:
        if movie["year"] > 1979 and movie["year"] < 1990 :
            genres = movie["genre"]
            genres_list_for_80.append(genres)
    print(genres_list_for_80)
    
    for genre in genres_list_for_80:
        if genre in genres_dict_for_80_appearing:
            genres_dict_for_80_appearing[genre] += 1
        else:
            genres_dict_for_80_appearing[genre] = 1
    print(genres_dict_for_80_appearing)
    
    genres_min = min(genres_dict_for_80_appearing.values())
    print(genres_min)
    
    for key in genres_dict_for_80_appearing:
        if genres_dict_for_80_appearing[key] == genres_min:
            genre_dict_least_popular[key] = genres_dict_for_80_appearing[key]
    print(genre_dict_least_popular)
    
    for keys in genre_dict_least_popular:
        print(f"\nLeast popular genre in the 1980's: {keys}\n")


if __name__ == "__main__":
    main()



