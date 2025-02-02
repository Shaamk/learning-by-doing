diameters = [10, 4, 83.2, 62, 33.3]

def main():
    '''
        The 'diameters' list is a list of diameters of circles.
        The diameter is in centimetres.
        For each circle, print out the area of the circle.
        The results should look like:
            Circle with diameter 10 has an area of ???
    '''
    results()


def results():
    for i in diameters:
        print(f"Circle with diameter {i} has an area of {2 * 3.14 * (i/2)}")



if __name__ == '__main__':
    main()