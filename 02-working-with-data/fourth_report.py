# List : List the name and year of all movies, separated by a comma.
# Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
# Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
# Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
# Quit : Ends the program.


from movie_data import movies


def main():
    show_main_menu()
    options_to_choose()    
    actor_search()


def show_main_menu():
    print("-"*20)
    print("1. List\n2. Actor search\n3. Genre search\n4. Adding\n5. End program")
    print("-"*20)
    options_to_choose()


def options_to_choose():
    option = input("select option: ")
    while not option == 5:
        if option == "1":            
            option = movies_list()
        if option == "2":
            option = actor_search(option)
        if option == "5":
            print("Ending")
            quit()

    
def movies_list():
    the_title_and_year_dict = {}
    for movie in movies:
        title = movie["title"]
        year = movie["year"]
        the_title_and_year_dict[title] = year
    
    for title, year in the_title_and_year_dict.items():
        print(f'{title}, {year}')
    return show_main_menu()


def actor_search():
    pass
    #for movie in movies:
    




if __name__ == '__main__':
    main()




