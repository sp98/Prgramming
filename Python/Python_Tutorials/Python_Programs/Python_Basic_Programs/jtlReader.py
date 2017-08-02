import csv
from collections import defaultdict

loc = '/Users/santosh/Downloads/Twitter-3.jtl'
#loc = '/Users/santosh/Downloads/Twitter-3.jtl'

col_headers = []
my_dict = {}
resp_dict = {}
test_data = []

j_total_tests = 0
j_total_passed = 0
j_total_failed = 0
j_test_date = ''
jtl_dict = {}
j_test_data = []

with open(loc, 'r') as jtl_file:
    data = csv.reader(jtl_file)
    col_headers = csv.DictReader(jtl_file).fieldnames
    rows = list(data)
    for index, row in enumerate(rows):
        if not row[col_headers.index('label')] in my_dict:
            label_data = []
            label_data.append(1)
            my_dict[row[col_headers.index('label')]] = label_data
        else:
            my_dict[row[col_headers.index('label')]][0] += 1

        if len(my_dict[row[col_headers.index('label')]]) == 1:
            if'false' in row[col_headers.index('success')]:
                my_dict[row[col_headers.index('label')]].append(1)
        else:
            if 'false' in row[col_headers.index('success')]:
                my_dict[row[col_headers.index('label')]][1] += 1

    for index, row in enumerate(rows):
        if not row[col_headers.index('label')] in resp_dict:
            resp_data = []
            resp_dict[row[col_headers.index('label')]] = resp_data
        resp_dict[row[col_headers.index('label')]].append(int(row[col_headers.index('elapsed')]))

    for keys in my_dict:
        if len(my_dict[keys]) == 1:
            my_dict[keys].append(0)
        passing = my_dict[keys][0]-my_dict[keys][1]
        my_dict[keys].insert(1, passing)

    for keys in resp_dict:
        my_dict[keys].append(float(sum(resp_dict[keys]) / len(resp_dict[keys])))


for key in my_dict:
    test_data.append(key)
    for data in my_dict[key]:
        test_data.append(data)


jtl_dict['Test_Data'] = j_test_data
jtl_dict['Total_Tests'] = j_total_tests
jtl_dict['Total_Pass'] = j_total_passed
jtl_dict['Total_Fail'] = j_total_failed
jtl_dict['Project_Name'] = str(j).split('/')[-3]
jtl_dict['Job_Number'] = str(jtlfile).split('/')[-2]
head, tail = os.path.split(jtlfile)
jtl_dict['Location'] = head + '/index.html'
jtl_dict['Test_Date'] = j_test_date
jtl_dict['Total_Cols'] = 5

print(test_data)







