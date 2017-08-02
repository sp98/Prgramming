import testDatabase
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

import testDatabase


report_time = None
total = 0
total_passed = 0
total_failed = 0
total_pending = 0
total_ignored = 0
total_time = 0

test_results = {}
# result_page = "file:///Users/santosh/eclipse/workspace/ \
#  "screenplay-pattern-todomvc-master/target/site/serenity/index.html"

# result_page = "file:///Users/santosh/eclipse/workspace/POMDemo/target/site/serenity/index.html"
# result_page = "file:///Users/santosh/eclipse/workspace/SerenityCucumber/target/site/serenity/index.html"

result_page = "file:///Users/santosh/eclipse/workspace/SnapchatUI/target/site/serenity/index.html"
page = urlopen(result_page)
soup = BeautifulSoup(page, "html.parser")


def get_results():
    count = 0;

    report_time = re.search(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', soup.find("span", "date-and-time").text).group()

    summary_table = soup.find("table", {"class": "summary-table"})

    for row in summary_table.findAll('tr'):
        count += 1
        cell = row.findAll('td')
        if count == 4:
            # print(cell[0].text)
            test_results["total"] = cell[1].text
            test_results["passed"] = cell[2].text
            test_results["failed"] = cell[3].text
            test_results["pending"] = cell[4].text
            test_results["ignored"] = cell[5].text
            test_results["date"] = report_time

        if count == 5:
            test_results["time"]= cell[1].text

    print("Dict: ", test_results)


if __name__ == '__main__':
    get_results()
    testDatabase.initialize_db()
    testDatabase.add_entries(test_results)
    print(testDatabase.get_entries())





