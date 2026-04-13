import json

def read_data(file_name, field):
    with open (file_name, 'r') as file:
        data = json.load(file)

    if field in data:
        return data[field]
    else:
        return None

def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)


def linear_search(sekvence, cislo):

    x = []
    for i, z in enumerate(sekvence):
        if z == cislo:
            x.append(i)

    return {'positions': x, 'count': len(x)}

def main():
    f = read_data('sequential.json', 'unordered_numbers')
    cislo = 8
    l = linear_search(f, cislo)

    print(f"Hľadané číslo: {cislo}")
    print(f"Výsledok: {l}")



def binary_search(seznam, cislo):


    l = 0
    r = len(seznam) - 1

    while l <= r:
        x = (l + r)//2
        if seznam[x] == cislo:
            return x
        elif cislo < seznam[x]:
            r= x - 1
        else:
            l = x -1
    return None

def main():

    m = read_data('sequential.json', 'unordered_numbers')
    if m:
        cislo = 8
        i = binary_search(m, cislo)

        print(f"Zoznam je: {m}")
        print(f"Hľadané číslo  je:{cislo} a je na indexe: {i}")
    else:
        print("Zlyhalo načítanie dát")

from generators import ordered_sequence
from searching import linear_search, binary_search

    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []

    for x in sizes:
        t = 1000

    r = time.perf_counter()
    linear_search(x, t)
    rr = time.perf_counter()
    linear_times.append(rr - r)

    s = time.perf_counter()
    binary_search(x, t)
    ss = time.perf_counter()
    binary_times.append(ss - s)



    import matplotlib.pyplot as plt

    plt.plot(sizes, linear_times)
    plt.plot(sizes, binary_times)
    plt.xlabel("velkost vstupu")
    plt.ylabel("cas s")
    plt.title("graf- ukazka")
    plt.show()


def pattern_search(sekvencia, patern):
    x = set()
    s = len(sekvencia)
    ss = len(patern)






if __name__ == "__main__":
    main()
