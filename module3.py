def read_file(path):
    """
    str -> list
    read lines from file with content about films
    """
    linelist = []
    with open(path, 'r') as filecontent:
        line = filecontent.readline()
        while not line.startswith("=============="):
            line = filecontent.readline()
        line = filecontent.readline()
        for line in filecontent:
            if line.startswith("--------------------"):
                break
            linelist.append(line.strip())
    return linelist


def country_dict(linelist, year):
    """
    (list, int) -> dict
    return dict ffrom list of lines with country as
    key and name as value
    """
    film_dict = {}
    for line in linelist:
        try:
            if int(line.split("\"")[2].split()[0].strip("()")) != year:
                continue
            country = line.split()[-1]
            film = line.split("\"")[1]
            if country in film_dict:
                film_dict[country].append(film)
            else:
                film_dict[country] = [film]
        except ValueError:
            continue
    return film_dict


def country_num(film_dict):
    """
    dict -> List
    return sorted list of tuples woth countries and number of films
    """
    film_list = []
    for country in film_dict:

        film_list.append((country, len(film_dict[country])))

    film_list.sort(key=lambda x: x[1], reverse=True)
    return film_list


def write_films(film_list):
    """
    list -> None
    write country and number of films to file
    """
    with open("films.txt", 'w') as write_file:
        for country in film_list:
            write_file.write(country[0] + "  " + str(country[1]) + '\n')


def films_year(year):
    """
    int -> None
    Writes to file films from the year sorted by number of films countries
    made in descending order
    """
    linelist = read_file("countries.list")
    film_list = country_num(country_dict(linelist, year))
    write_films(film_list)


if __name__ == "__main__":
    try:
        year = int(input("Print year:"))
        films_year(year)
    except ValueError:
        print("wrong input")
