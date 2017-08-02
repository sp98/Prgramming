import csv

with open('myfile.csv', 'a') as file:
    fieldNames = ['Col1', 'Col2', 'Col3', 'Col4']
    csvWriter = csv.DictWriter(file, delimiter=',', fieldnames=fieldNames)
    csvWriter.writeheader()  # add a check to add header only if the file exists
    csvWriter.writerow({'Col1': 'Pramod', 'Col2': 'Rautela', 'Col3': 54, 'Col4': 'Test'})
