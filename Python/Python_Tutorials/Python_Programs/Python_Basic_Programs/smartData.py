import sys
import os
import csv
from collections import defaultdict


class FailureReport:

    loc = ''

    def __init__(self, data_loc):
        self.loc = data_loc

    def get_files(self):
        file_dict = defaultdict(list)
        for root, dirs, files in os.walk(self.loc, topdown=True):
            for file_name in files:
                if 'results.csv' in file_name and '~lock.results.csv' not in file_name:
                    head, tail = os.path.split(os.path.dirname(root))
                    file_dict[tail].append(os.path.join(root, file_name))

        return file_dict

    def get_failures(self, file_dict):
        result_list = []

        for test_name in file_dict.keys():
            test_dict = {}
            detail_list = []
            test_dict['name'] = test_name
            detail_dict = {}
            for index, csv_path in enumerate(reversed(file_dict[test_name])):
                with open(csv_path, 'r') as csv_file:
                    col_headers = csv.DictReader(csv_file).fieldnames
                    data = csv.reader(csv_file)

                    for row_data in list(data):

                        if 'ERROR' in row_data[col_headers.index('Result')] or 'FAILURE' in row_data[col_headers.index('Result')]:
                            if index == 0 and len(detail_dict) == 0:
                                detail_dict = {}
                                detail_dict['scenario'] = row_data[col_headers.index('Title')]
                                detail_dict['feature'] = row_data[col_headers.index('Story')]
                                detail_dict['count'] = 1
                                detail_list.append(detail_dict)
                            elif index == 0 and not any(data.get('scenario', None) == row_data[col_headers.index('Title')] for data in detail_list):
                                detail_dict = {}
                                detail_dict['scenario'] = row_data[col_headers.index('Title')]
                                detail_dict['feature'] = row_data[col_headers.index('Story')]
                                detail_dict['count'] = 1
                                detail_list.append(detail_dict)
                            elif any(data.get('scenario', None) == row_data[col_headers.index('Title')] for data in detail_list):
                                for data in detail_list:
                                    if data['scenario'] == row_data[col_headers.index('Title')]:
                                        data['count'] += 1
                if index == 0 and len(detail_list) == 0:
                    print('No errors in the latest Build for test - ' + test_name)
                    break
                else:
                    continue

            test_dict['detail'] = detail_list
            result_list.append(test_dict)

        print(result_list)
        return result_list


if __name__ == '__main__':
    args = sys.argv
    if len(args)<2:
        print("Please provide the Test data directory")
        exit()
    elif not os.path.isdir(args[1]):
        print('The Location \'{}\' is not correct'.format(args[1]))
        exit()
    else:
        report = FailureReport(args[1])

    report.get_failures(report.get_files())
