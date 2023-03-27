
# Actor appearring in most movies: Julia Roberts
# Actor with best average rating: Jean Claude Van Damme
# Least popular genre in the 1980's: music videos



from movie_data import movies


def main():
    actor_appearing_most()
 
        
# count the appearance of the actor in each movie
def actor_appearing_most():
    Mark_Hamill = 0
    Harrison_ford = 0
    Matthew_Broderick = 0
    appearing_numbers = [0, 0, 0]
    for movie in movies:
        actors = movie["actors"]
        if "Mark Hamill" in movie["actors"]:
            appearing_numbers[0] += 1
        if "Harrison Ford" in movie["actors"]:
            appearing_numbers[1] += 1
        if "Matthew Broderick" in movie["actors"]:
            appearing_numbers[2] += 1
        # if .. in movie["actors"]:
        #     .. += 1

        
            

        # for actor in actors:
        #     if actor in movies:
        #         appearance_of_actor += 1
    print(appearing_numbers)                
    # print(Mark_Hamill)
    # print(Harrison_ford)
    # print(Matthew_Broderick)
            

# HET GING OM HET VOOR ELKAAR KRIJGEN VAN DIT:            
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
    print(f"Actor appearing in most movies: {maximum_appearing}\n")
    return actors_appearing
                




if __name__ == "__main__":
    main()

