from urllib import request
from bs4 import BeautifulSoup
from urllib.error import HTTPError

site = input("Enter the site you would like to analyze for keywords: ")
keyword_file = open('keywords.txt', 'r')

def keyword_checker():
    result_list = []
    try:
        site_content = request.urlopen(site)
    except HTTPError as e:
        print(e)

    data = BeautifulSoup(site_content, 'html.parser')
    print('data', data)

    for each_line in keyword_file:
        print('each_line', each_line)
        stripped_line = each_line.strip()

        result_list = data.body.findAll(text=stripped_line)
        print('result_list', result_list)

    
    return result_list

print(keyword_checker())