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




if __name__ == "__main__":
    main()
