def main():
    data = getting_the_text_data()
    movies_list = storing(data)
    database(movies_list)


def getting_the_text_data():
    with open('20-03-23-working-with-files/movie_data.txt', 'rt') as movies:
        data = movies.read()
        return data
        #print(movies.read())


def storing(data):
    movies_list = []
    movies_list = data.splitlines()
    #print(movies_list)
    return movies_list
    

def database(movies_list):
    output_list = []
    for i in range(len(movies_list)):
        if i % 5 == 0:
            movie = {}
            movie["title"] = movies_list.pop(0)
            movie["actors"] = movies_list.pop(0)
            movie["year"] = movies_list.pop(0)
            movie["genre"] = movies_list.pop(0)
            movie["rating"] = movies_list.pop(0)        
            output_list.append(movie)
    print(output_list)

 
    


if __name__ == '__main__':
    main()


# for loop 
# dictionary