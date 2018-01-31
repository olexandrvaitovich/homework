import collections


def read_file(path):
    with open(path, "r", encoding="utf-8", errors='ignore') as file:
        file.readline()
        new_f = (file.read().split("\n"))

    return set(new_f)


def votes_dict(lines_set, num_v):
    dct = dict()
    for line in lines_set:
        if int(line.split("\t")[2]) > num_v:
            dct[line.split("\t")[2]] = line
    return dct


def firms_id(n, dict_votes):
    film_set = set()
    ordered_dict = collections.OrderedDict(sorted(dict_votes.items()))
    for i in range(1, n + 1):
        film_set.add(dict_votes[list(ordered_dict)[-i]])
    return film_set


def write_films_id(set_films_id):
    with open("result.txt", "w") as file:
        file.write(str(set_films_id))


def find_films_id(n, num_v):
    return firms_id(n, votes_dict(read_file("title.ratings.tsv.gz"), num_v))


print(find_films_id(10, 1000))
