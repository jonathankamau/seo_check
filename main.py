from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError

site = input("Enter the site you would like to analyze for keywords: ")
keyword_file = open('keywords.txt', 'r')

def keyword_checker():
    # result_list = []
    try:
        site_content = request.urlopen(site).read()
    except HTTPError as e:
        print(e)

    data = BeautifulSoup(site_content)
    print('data', data)

    for each_line in keyword_file:
        print('each_line', each_line.lower())
        stripped_line = each_line.lower().strip()

        result_list = data.find_all('p', string=stripped_line)
        print('result_list', result_list)



keyword_checker()