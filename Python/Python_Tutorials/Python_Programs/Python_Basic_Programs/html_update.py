import os, sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

qa_dashboard_url = 'http://172.16.11.219:5000'


def update_html(loc):
    '''
    Updates the index.html file for Serenity or Jmeter report in the
    tomcat server to have a link back to the QADashboard.
    :param loc: The location of the index.html file in Serenity or JMeter Report
    :return: N/A
    '''
    for file in os.listdir(loc):
        if 'index.html' in file:
            file_path = loc+'/'+file.replace("\\", '/')
            print('Updating file : ' + '\'' + file_path + '\'')
            html_page = urlopen("file://" + file_path)
            soup = BeautifulSoup(html_page, "html.parser")
            try:
                for a_tag in soup.findAll("div", {"id": "logo"}):
                    a_tag.find('a')['href'] = qa_dashboard_url

            except KeyError:
                print('Not Found')

            try:
                for a_tag in soup.findAll("a", {"class": "navbar-brand"}):
                    a_tag['href'] = qa_dashboard_url

            except KeyError:
                print('Not found')

            html_page = soup.prettify('utf-8')
            with open(file_path, "wb") as file:
                file.write(html_page)

if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 1:
        print('Please provide the location(s) for Serenity Report(s) or Jtl Report')

    for index, arg in enumerate(args):
        if index == 0:
            continue
        if not os.path.isdir(arg):
            print("Path \'{}\' does not exist. Please provide"
                  "a correct path for the root directory.".format(args[1]))
            continue
        else:
            update_html(arg)
