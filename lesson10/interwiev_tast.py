import csv

def calc_people(filename):
    country={}
    with open(filename, "r") as file:
        people=csv.DictReader(file)
        for line in people:
            if line["country"] not in country.keys():
                name_tmp = []
            else:
                name_tmp = country[line["country"]]["people"]
            name_tmp.append(line["person"])
            count_tmp=len(name_tmp)
            country[line["country"]] = {"people": name_tmp, "count": count_tmp}
        return country




def main():
    data_file="data.csv"
    print(calc_people(data_file))


if __name__ == '__main__':
    main()