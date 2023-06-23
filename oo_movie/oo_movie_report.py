#from movie_data import movies

class Movie:
    def __init__(self, title, actors, year, genre, rating):
        self.title = title
        self.actors = actors
        self.year = year
        self.genre = genre
        self.rating = rating

    def __lt__(self, other):    # lower than
        return self.rating < other.rating
    
    def __gt__(self, other):    # greater than
        return self.rating > other.rating


class MovieCollection:
    def __init__(self, movies):
        self._collection = []
        if movies:
            for movie in movies:
                self._collection.append(movie)
    
    # def __str__(self): # works
    #     return f"The total numbers of movies : {len(self.collection)} movies."

    def number_of_movies(self):
        return f"Total numbers of movies: {len(self._collection)} movies."


    def average_rating(self):
        total = 0
        for movie in self._collection:
            total += movie.rating
        return f"Average rating of movies: {total / len(self._collection)}"

    
    def best_movie_first_way(self):
        best_rating = 0
        for movie in self._collection:
            if movie.rating > best_rating:
                best_rating = movie.rating
                best_movie = movie.title
        return f"The best movie first way: {best_movie}"


    def worst_movie_first_way(self):
        worst_rating = 10
        for movie in self._collection:
            if movie.rating < worst_rating:
                worst_rating = movie.rating
                worst_movie = movie.title
        return f"The worst movie first way: {worst_movie}"
    
    
    def best_movie_second_way(self):
        the_best_movie = None
        for movie in self._collection:
            if the_best_movie is None or the_best_movie < movie:
                the_best_movie = movie
        return f"The best movie second way: {the_best_movie.title} with a rating of: {the_best_movie.rating}"
    

    def worst_movie_second_way(self):
        the_worst_movie = None
        for movie in self._collection:
            if the_worst_movie is None or the_worst_movie > movie:
                the_worst_movie = movie
        return f"The worst movie second way: {the_worst_movie.title} with the rating of: {the_worst_movie.rating}"
    

    def best_movie_third_way(self):
        the_best_movie = self._collection[0]
        for movie in self._collection[1:]:
            if the_best_movie < movie:
                the_best_movie = movie
        return f"The best movie third way: {the_best_movie.title} with a rating of: {the_best_movie.rating}"


    def worst_movie_third_way(self):
        the_worst_movie = self._collection[0]
        for movie in self._collection[1:]:
            if the_worst_movie > movie:
                the_worst_movie = movie
        return f"The worst movie third way: {the_worst_movie.title} with the rating of: {the_worst_movie.rating}"
    

    def best_movie_max(self):
        pass
        # for movie in self.collection:
        #     if movie.rating == max(self.collection.rating):
        #         best_movie = movie.rating
        # return f"The max best movie: {best_movie.title}"


    def worst_movie_min(self):
        pass
        # worst_movie = min(self.collection, key=lambda self.collection:self.collection.rating)
        # return f"The min best movie: {worst_movie.title}"
    


    # worst = min(movies, key=lambda x:x["rating"])
    # print(f'The LAMBDA worst movie: {worst["title"]}')





movies = [
    Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7),
    Movie("Star Wars Episode I: The Phantom Menace", ["Liam Neeson", "Ewan McGregor", "Natalie Portman", "Jake Lloyd", "Brian Blessed"], 1999, "science fiction", 3),
    Movie("Star Trek IV: The Voyage Home", ["William Shatner", "Leonard Nimoy", "Michelle Nichols"], 1986, "science fiction", 8),
    Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9),
    Movie("The Naked Gun: From The Files Of Police Squad!", ["Leslie Nielsen", "O. J. Simpson", "Priscilla Presley"], 1988, "comedy", 8),
    Movie("Leprechaun", ["Warwick Davis", "Jennifer Aniston"], 1993, "horror", 6),
    Movie("Leprechaun 4: In Space", ["Warwick Davis"], 1996, "horror", 10),
    Movie("Flash Gordon", ["Brian Blessed", "Timothy Dalton", "Max von Sydow"], 1980, "science fiction", 6),
    Movie("The Rock", ["Nicolas Cage", "Sean Connery", "Ed Harris", "Michael Biehn"], 1996, "action", 8),
    Movie("Con Air", ["Nicolas Cage", "John Malkovich", "John Cusack", "Steve Buscemi", "Ving Rhames"], 1997, "action", 9),
    Movie("Airheads", ["Brendan Fraser", "Adam Sandler", "Steve Buscemi", "Judd Nelson", "Lemmy Kilmister"], 1994, "comedy", 5),
    Movie("The Breakfast Club", ["Judd Nelson", "Emilio Estevez", "Ally Sheedy", "Molly Ringwald"], 1985, "drama", 6),
    Movie("Wargames", ["Matthew Broderick", "Ally Sheedy"], 1983, "drama", 8),
    Movie("Godzilla", ["Matthew Broderick", "Jean Reno"], 1998, "action", 6),
    Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 9),
]


my_collection = MovieCollection(movies)
print(my_collection.number_of_movies())
print(my_collection.average_rating())
print(my_collection.best_movie_first_way())
print(my_collection.worst_movie_first_way())
print(my_collection.best_movie_second_way())
print(my_collection.worst_movie_second_way())
print(my_collection.best_movie_third_way())
print(my_collection.worst_movie_third_way())
print(my_collection.best_movie_max())
print(my_collection.worst_movie_min())