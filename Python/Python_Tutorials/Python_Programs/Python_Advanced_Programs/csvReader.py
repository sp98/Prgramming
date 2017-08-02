import csv

def csv_list_reader():
    with open('myfile.csv') as file:
        csvReader = csv.reader(file, delimiter=',') # this returns a generator so can't use index
        rows = list(csvReader)
        for row in rows:
            print(row)
            #print(', '.join(row))

def csv_dict_reader():
    with open('myfile.csv') as file:
        csvReader = csv.DictReader(file, delimiter=',')
        rows = list(csvReader)
        for row in rows:
            print(row)


csv_list_reader()
csv_dict_reader()
